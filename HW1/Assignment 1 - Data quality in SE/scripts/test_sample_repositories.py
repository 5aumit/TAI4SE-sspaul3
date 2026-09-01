import sys
import unittest
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from sample_repositories import select_files, select_repositories


class SampleRepositoryTests(unittest.TestCase):
    def test_repository_selection_is_stable_and_requires_five_files(self):
        counts = Counter({"a/repo": 5, "b/repo": 6, "c/repo": 8, "d/repo": 4})
        selected = select_repositories(counts, seed=591, repository_count=3)

        self.assertEqual(selected, select_repositories(counts, seed=591, repository_count=3))
        self.assertNotIn("d/repo", selected)

    def test_file_selection_caps_and_is_stable(self):
        rows = [
            {"repo_name": "a/repo", "blob_id": f"blob-{number}", "path": f"/{number}.py"}
            for number in range(10)
        ]

        selected = select_files(rows, seed=591, files_per_repository=3)

        self.assertEqual(len(selected), 3)
        self.assertEqual(selected, select_files(rows, seed=591, files_per_repository=3))
