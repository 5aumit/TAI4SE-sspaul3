import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from review_candidates import load_pairs, selected_pair_ids, write_candidates, write_review


class ReviewCandidatesTests(unittest.TestCase):
    def test_review_checkbox_builds_two_assignment_records(self):
        pair = {
            "repo_name": "owner/repo",
            "jaccard_similarity": 0.8,
            "left": self.record("left", "repos/001/001.py"),
            "right": self.record("right", "repos/001/002.py"),
        }
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            sample = root / "sample"
            for record in (pair["left"], pair["right"]):
                local_file = sample / record["local_file"]
                local_file.parent.mkdir(parents=True, exist_ok=True)
                local_file.write_text("print('duplicate')\n", encoding="utf-8")
            pairs_path = sample / "duplication-pairs.jsonl"
            pairs_path.write_text(json.dumps(pair) + "\n", encoding="utf-8")
            review = sample / "review.md"
            write_review(load_pairs(pairs_path), sample, review, 1)
            review.write_text(review.read_text(encoding="utf-8").replace("[ ] Candidate pair 001", "[x] Candidate pair 001"), encoding="utf-8")

            output = root / "candidates.jsonl"
            self.assertEqual(write_candidates(selected_pair_ids(review), load_pairs(pairs_path), output), 2)
            candidates = [json.loads(line) for line in output.read_text(encoding="utf-8").splitlines()]

        self.assertEqual([candidate["blob_id"] for candidate in candidates], ["left", "right"])
        self.assertEqual(candidates[0]["revision_id"], "revision")
        self.assertIn("0.800", candidates[0]["flag_reason"])
        self.assertIn("right", candidates[0]["flag_reason"])

    @staticmethod
    def record(blob_id, local_file):
        return {
            "blob_id": blob_id,
            "src_encoding": "UTF-8",
            "repo_name": "owner/repo",
            "path": f"/{blob_id}.py",
            "revision_id": "revision",
            "local_file": local_file,
        }
