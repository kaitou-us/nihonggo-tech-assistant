from collections import Counter

def analyze_vocabulary(words: list[str]) -> dict[str]:
    """分析词汇列表，返回词频统计结果。"""
    counter = Counter(words)
    total = len(words) #总词汇数
    unique = len(counter) #唯一词汇数
    duplicates = {word: count for word, count in counter.items() if count > 1}
    ranked = counter.most_common()
    return {
        "total": total,
        "unique": unique,
        "duplicates": duplicates,
        "ranked": ranked
    }