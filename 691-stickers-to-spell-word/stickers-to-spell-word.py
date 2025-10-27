class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        target_count = Counter(target)
        # Preprocess stickers: only keep chars that are in target
        stickers_count = [Counter(s) & target_count for s in stickers]
        stickers_count = [s for s in stickers_count if s]  # remove empty stickers

        start = ''.join(sorted(target))  # initial state
        queue = deque([(start, 0)])
        visited = set()
        visited.add(start)

        while queue:
            remain, used = queue.popleft()
            if not remain:
                return used  # done

            remain_count = Counter(remain)

            for sticker in stickers_count:
                # Optimization: skip stickers that don't contain first needed char
                if remain[0] not in sticker:
                    continue

                # Apply sticker
                new_count = remain_count - sticker
                new_remain = ''.join(sorted(char * cnt for char, cnt in new_count.items()))

                if new_remain not in visited:
                    visited.add(new_remain)
                    queue.append((new_remain, used + 1))

        return -1  # impossible