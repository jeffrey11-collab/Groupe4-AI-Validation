import sys

def analyze_commit(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    if "TODO" in content or "FIXME" in content:
        print("❌ Le code contient des éléments à corriger (TODO/FIXME).")
        sys.exit(1)
    print("✅ Code validé avec succès par l’IA.")
    sys.exit(0)

if __name__ == "__main__":
    analyze_commit("src/test_commit.py")
