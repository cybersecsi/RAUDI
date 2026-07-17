import subprocess
from datetime import date
from pathlib import Path


AUTOCOMMIT_SCRIPT = (
    Path(__file__).resolve().parents[1] / ".github" / "workflows" / "autocommit.sh"
)


def test_autocommit_writes_successful_updates(tmp_path):
    log_file = tmp_path / "raudi.log"
    updated_images_file = tmp_path / "updated-images.txt"
    changelog_file = tmp_path / "LOG.md"
    log_file.write_text(
        "[+] secsi/first:1.2.3 successfully pushed to Docker Hub\n"
        "[-] Unable to build secsi/broken:2.0\n"
        "[+] secsi/second:4.5 successfully pushed to Docker Hub\n"
        "[+] RAUDI completed, exiting with return code 1\n"
    )
    changelog_file.write_text("# Updates\n")

    subprocess.run(
        [
            "bash",
            str(AUTOCOMMIT_SCRIPT),
            str(log_file),
            str(updated_images_file),
            str(changelog_file),
        ],
        check=True,
    )

    assert changelog_file.read_text() == (
        "# Updates\n"
        f"\n### [{date.today().isoformat()}]\n"
        "- secsi/first updated to version 1.2.3\n"
        "- secsi/second updated to version 4.5\n"
    )


def test_autocommit_leaves_changelog_unchanged_without_updates(tmp_path):
    log_file = tmp_path / "raudi.log"
    updated_images_file = tmp_path / "updated-images.txt"
    changelog_file = tmp_path / "LOG.md"
    log_file.write_text("[+] RAUDI completed, exiting with return code 1\n")
    changelog_file.write_text("# Updates\n")

    subprocess.run(
        [
            "bash",
            str(AUTOCOMMIT_SCRIPT),
            str(log_file),
            str(updated_images_file),
            str(changelog_file),
        ],
        check=True,
    )

    assert changelog_file.read_text() == "# Updates\n"
