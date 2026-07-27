class Solution:
    def leastInterval(self, tasks, n):
        count = Counter(tasks)
        max_count = max(count.values())
        max_tasks = sum(1 for c in count.values() if c == max_count)
        return max(len(tasks), (max_count - 1) * (n + 1) + max_tasks)