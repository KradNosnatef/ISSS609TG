class RawComment:
    def __init__(self,comment):
        self.RID=int(comment[0])
        self.rating=comment[1]
        self.yearMonth=comment[2]   #this is YM's raw string
        self.reviewerLocation=comment[3]
        self.branch=comment[5]

    def getYearMonthInQueryFormat(self):
        if self.yearMonth=="missing":
            return("1970-01-01")
        
        list=self.yearMonth.split("-")
        if len(list[1])==1:
            list[1]="0"+list[1]
        
        return(list[0]+"-"+list[1]+"-01")