class RawComment:
    def __init__(self,comment):
        self.RID=int(comment[0])
        self.rating=comment[1]
        self.yearMonth=comment[2]   #this is YM's raw string
        self.reviewerLocation=comment[3]
        