# Get the real map of China
library(jsonlite)
library(rjson)
library(tidyverse)
library(lubridate)
load("~/Desktop/PhDwork/Py-Github/Piao/IBM.Rdata")
# read.json
df=read_json("300435.txt")
x=df$data
y=x$klines
name=x$name
# get data
dfprice=c()
for (i in 1:length(y)) {
  id=i
  value=y[[i]]
  yy=tibble(id=id,value=value)
  dfprice=rbind(dfprice,yy)
}
# rename data
df=dfprice %>% select(-id) %>% 
  separate(value,c("time","kaipan","shoupan","high","low","tradenumber","trademoney","zhenfu","todayindex","todaydiff","changerate")
           , sep = "([,])")
# remove
rm(i,yy,x,y,dfprice)

write.csv(df,"df.csv")
df=read.csv("df.csv",header = T) %>% as_tibble() %>% 
  mutate(time=as.Date(time)) %>% 
  arrange(desc(time))

# remove file
file.remove("df.csv")


## plot
library(sysfonts)
library(showtextdb)
library(showtext)

showtext_auto()
ggplot(df)+
  geom_point(aes(time,low))+
  geom_line(aes(time,low))+
  labs(title = name)


df1=df %>% filter(time>as.Date("2021-03-18"))
df2=df %>% filter(time>as.Date("2021-03-18"))
ggplot(df1)+
  geom_point(aes(time,low))+
  geom_line(aes(time,low))+
  geom_line(data=df2,aes(time,high,color="red"))+
  labs(title = name)+ 
  geom_hline(yintercept=0.5*max(df$kaipan), linetype="dashed", color = "red", size=1)+
  geom_hline(yintercept=0.5*max(df$shoupan), linetype="dashed", color = "blue", size=1)









