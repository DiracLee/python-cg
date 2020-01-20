
def area2(p, q, r):
    # The area value of triangle<p, q, r>
    return p.x * q.y - p.y * q.x + q.x * r.y - q.y * r.x + r.x * p.y - r.y * p.x

def to_left(p, q, s):
    # Whether point s is on the left of direted line p->q
    return area2(p, q, s) > 0

def in_triangle(p, q, r, s):
    # Whether point s is inside the triangle<p, q, r>
    pq_left = to_left(p, q, s)
    qr_left = to_left(q, r, s)
    rp_left = to_left(r, p, s)
    return pq_left==qr_left and rp_left==pq_left
    