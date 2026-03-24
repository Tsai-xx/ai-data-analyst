from analyzer import analyze_data
from report_generator import generate_report

def main():
    file_path = "sample.csv"

    summary = analyze_data(file_path)
    report = generate_report(summary)

    print("\n=== AI REPORT ===\n")
    print(report)

if __name__ == "__main__":
    main()