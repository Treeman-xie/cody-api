# generator.py

def generate_code(prompt: str) -> str:
    """
    根据自然语言描述生成代码（模拟版本）
    """
    prompt = prompt.lower()

    if "bubble sort" in prompt or "冒泡排序" in prompt:
        return """
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
        """.strip()
    
    elif "fibonacci" in prompt or "斐波那契" in prompt:
        return """
def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]
        """.strip()

    else:
        return "# TODO: 请提供更具体的编程任务描述"
