import bisect

def activityNotifications(expenditure, d):
    from collections import deque

    def get_median(freq, d):
        count = 0
        if d % 2 == 1:
            median_pos = d // 2 + 1
            for i in range(201):
                count += freq[i]
                if count >= median_pos:
                    return i
        else:
            first = None
            second = None
            median_pos1 = d // 2
            median_pos2 = median_pos1 + 1
            for i in range(201):
                count += freq[i]
                if first is None and count >= median_pos1:
                    first = i
                if count >= median_pos2:
                    second = i
                    break
            return (first + second) / 2

    freq = [0] * 201
    for val in expenditure[:d]:
        freq[val] += 1

    notifications = 0
    for i in range(d, len(expenditure)):
        median = get_median(freq, d)
        if expenditure[i] >= 2 * median:
            notifications += 1
        # atualizar janela
        freq[expenditure[i - d]] -= 1
        freq[expenditure[i]] += 1

    return notifications

# Teste:
expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]
d = 5
print(activityNotifications(expenditure, d))
