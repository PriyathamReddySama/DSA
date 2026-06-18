class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minute_angle = minutes * 6  # 360/60
        hour_angle = (hour % 12) * 30 + minutes * 0.5  # 360/12 + (30/60)*minutes
        
        diff = abs(hour_angle - minute_angle)
        return min(diff, 360 - diff)