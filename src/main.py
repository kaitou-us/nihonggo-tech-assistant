from src.analyzer import analyze_vocabulary
from src.file_handler import read_vocabulary
from src.reporter import format_report, save_report

def main():
    file_path = "data/vocabulary.txt"
    words = read_vocabulary(file_path)
    results = analyze_vocabulary(words)
    report_content = format_report(results)
    save_report(report_content, "reports/report.txt")
    return results

if __name__ == "__main__":
    results = main()
    print(results)