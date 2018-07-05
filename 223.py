class Solution:
    def computeArea(self, a, b, c, d, e, f, g, h):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        # I'm so crazy because I try to list all conditions
        return (
            (d - b) * (c - a) + (h - f) * (g - e)
            if c <= e or d <= f or g <= a or h <= b
            else (d - b) * (c - a) + (h - f) * (g - e) - (min(c, g) - max(a, e)) * (min(d, h) - max(b, f))
        )
