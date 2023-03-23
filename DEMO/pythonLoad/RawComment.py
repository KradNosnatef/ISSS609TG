class RawComment:
    def __init__(self,comment):
        self.RID=int(comment[1])
        self.rating=int(comment[2])
        self.yearMonth=comment[3]   #this is YM's raw string
        self.reviewerLocation=comment[4]
        self.reviewText=comment[5]
        if len(self.reviewText)>8000:self.reviewText=self.reviewText[:8000]
        self.branch=comment[6]
        self.dominantTopic=int(comment[7])
        self.featureName="no way"
        self.sentiment="positive" if self.rating>=4 else "negative"

    def getYearMonthInQueryFormat(self):
        if self.yearMonth=="missing":
            return("1970-01-01")
        
        list=self.yearMonth.split("-")
        if len(list[1])==1:
            list[1]="0"+list[1]
        
        return(list[0]+"-"+list[1]+"-01")