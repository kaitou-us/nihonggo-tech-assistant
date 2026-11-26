from pathlib import Path
from datetime import datetime

def format_report(results: dict) -> str:
    #将词汇分析结果格式化为文本报告
    report_lines = ["========================================"]
    report_lines.append("Nihonggo Tech Assistant 词汇分析报告 - Developer A")
    report_lines.append("========================================")
    report_lines.append(f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report_lines.append(f"总词汇数: {results['total']}")
    report_lines.append(f"唯一词汇数: {results['unique']}")
    report_lines.append("重复词汇:")
    if not results['duplicates']:
        report_lines.append("  无重复词汇")
    else:
        for word, count in results['duplicates'].items():
            report_lines.append(f"  {word}: {count}")
    report_lines.append("词频排名:")
    for i, (word, count) in enumerate(results['ranked'], start=1):
        report_lines.append(f"  {i}. {word}: {count}")
    return "\n".join(report_lines)

def save_report(content: str, file_path: str) -> None:
    path = Path(file_path)
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    except OSError as e:
        raise OSError(f"无法写入报告文件: {path}") from e