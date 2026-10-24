"""
Safe File Organizer (Project 03)

Organizes unorganized folders by categorizing files into extension-based directories.
Implements:
- pathlib for safe, cross-platform path handling
- Dry-run mode for previewing operations without disk mutation
- Non-destructive collision resolution (file_1.ext, file_2.ext)
- Audit log in JSON format for rollback and verification
"""

import argparse
import json
import logging
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

# File extension categorization map
EXTENSION_CATEGORIES: Dict[str, str] = {
    # Documents
    ".pdf": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".md": "Documents",
    ".csv": "Documents",
    ".xlsx": "Documents",
    # Images
    ".png": "Images",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".gif": "Images",
    ".webp": "Images",
    ".svg": "Images",
    # Code
    ".py": "Code",
    ".js": "Code",
    ".ts": "Code",
    ".html": "Code",
    ".css": "Code",
    ".json": "Code",
    # Archives
    ".zip": "Archives",
    ".tar": "Archives",
    ".gz": "Archives",
    # Media
    ".mp3": "Media",
    ".mp4": "Media",
    ".mkv": "Media",
    ".wav": "Media",
}

DEFAULT_CATEGORY = "Miscellaneous"


@dataclass
class OrganizeAction:
    source_path: str
    target_path: str
    category: str
    file_size_bytes: int
    executed: bool
    timestamp: str


class FileOrganizer:
    """Safely sorts files into categorized folders with collision prevention."""

    def __init__(self, target_directory: Path, dry_run: bool = False):
        self.directory = Path(target_directory).resolve()
        self.dry_run = dry_run
        self.actions: List[OrganizeAction] = []

        if not self.directory.exists() or not self.directory.is_dir():
            raise ValueError(f"Directory does not exist or is not a directory: {self.directory}")

    def get_category_for_file(self, file_path: Path) -> str:
        """Return the category folder name based on extension."""
        suffix = file_path.suffix.lower()
        return EXTENSION_CATEGORIES.get(suffix, DEFAULT_CATEGORY)

    def resolve_destination(self, target_folder: Path, original_name: str) -> Path:
        """
        Generate collision-free destination path.
        If file.ext exists, returns file_1.ext, file_2.ext, etc.
        """
        candidate = target_folder / original_name
        if not candidate.exists():
            return candidate

        stem = Path(original_name).stem
        suffix = Path(original_name).suffix
        counter = 1

        while candidate.exists():
            candidate = target_folder / f"{stem}_{counter}{suffix}"
            counter += 1

        return candidate

    def organize(self) -> List[OrganizeAction]:
        """Scan directory and organize files into category folders."""
        self.actions.clear()

        # Gather files directly inside the root directory (do not recurse into category folders)
        files = [
            f for f in self.directory.iterdir()
            if f.is_file() and not f.name.startswith(".") and f.name != "organize_audit.json"
        ]

        for source_file in sorted(files):
            category = self.get_category_for_file(source_file)
            target_folder = self.directory / category
            destination_path = self.resolve_destination(target_folder, source_file.name)

            action = OrganizeAction(
                source_path=str(source_file),
                target_path=str(destination_path),
                category=category,
                file_size_bytes=source_file.stat().st_size,
                executed=not self.dry_run,
                timestamp=datetime.now().isoformat()
            )

            if not self.dry_run:
                target_folder.mkdir(parents=True, exist_ok=True)
                source_file.rename(destination_path)

            self.actions.append(action)

        if not self.dry_run and self.actions:
            self._save_audit_log()

        return self.actions

    def _save_audit_log(self) -> None:
        """Write JSON audit log of performed actions."""
        log_path = self.directory / "organize_audit.json"
        payload = [asdict(a) for a in self.actions]
        with open(log_path, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2)


def main():
    parser = argparse.ArgumentParser(description="Safely organize directory by file extensions.")
    parser.add_argument("path", help="Directory path to organize")
    parser.add_argument("--dry-run", action="store_true", help="Preview moves without touching files")
    args = parser.parse_args()

    organizer = FileOrganizer(Path(args.path), dry_run=args.dry_run)
    actions = organizer.organize()

    mode_label = "[DRY RUN]" if args.dry_run else "[EXECUTED]"
    print(f"\n{mode_label} Processed {len(actions)} files in: {organizer.directory}")
    for act in actions:
        print(f" -> {Path(act.source_path).name} => [{act.category}] {Path(act.target_path).name}")


if __name__ == "__main__":
    main()
