
class Route():

    def __init__(self, points):
        self.points = self.set_points(points)

    def set_points(self, points):
        return [complex(point[0], point[1]) for point in points]

    def get_points(self):
        return [(point.real, point.imag) for point in self.points]

    def get_total_distance(self):
        distance = 0
        for k in range(1, len(self.points)):
            p1 = self.points[k-1]
            p2 = self.points[k]
            distance += abs(p2 - p1)
        return distance

    def get_aerial_distance(self):
        return abs(self.points[0] - self.points[-1])

    def __repr__(self):
        return "Total distance: {}, aerial distance: {}".format(
            self.get_total_distance(),
            self.get_aerial_distance(),
        )

if __name__ == '__main__':
    p = [(1, 1), (5, 5), (8, -10), (-1, -1), (2, 2)]
    r = Route(p)
    print(r)
    print(r.get_points())