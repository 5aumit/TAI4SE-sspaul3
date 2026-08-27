import tempfile
import unittest
from pathlib import Path

from detect_duplication import detect, jaccard, token_ngrams


class DuplicationDetectorTests(unittest.TestCase):
    def test_overlapping_ngrams_ignore_comments_and_layout(self):
        with tempfile.TemporaryDirectory() as directory:
            left = Path(directory, "left.py")
            right = Path(directory, "right.py")
            left.write_text("result = price + 10\nprint(result)\n", encoding="utf-8")
            right.write_text("# ignored\nresult=price+10\n\nprint(result)\n", encoding="utf-8")

            grams = token_ngrams(left)
            self.assertEqual(grams, token_ngrams(right))
            self.assertEqual(len(grams), 5)
            self.assertEqual(jaccard(grams, grams), 1.0)

    def test_detect_skips_tokenization_failure(self):
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            folder.joinpath("a.py").write_text("result = price + 10\n", encoding="utf-8")
            folder.joinpath("b.py").write_text("result=price+10\n", encoding="utf-8")
            folder.joinpath("broken.py").write_text("value = '''unfinished\n", encoding="utf-8")

            matches, scores, errors = detect(folder, 0.70)

            self.assertEqual(matches, [("a.py", "b.py", 1.0)])
            self.assertEqual(scores, matches)
            self.assertEqual(errors[0][0], "broken.py")


if __name__ == "__main__":
    unittest.main()
