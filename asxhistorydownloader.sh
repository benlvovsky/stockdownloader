#!/bin/bash

savedir='floatdatadownload'
if [ -d "$savedir" ]; then rm -Rf $savedir; fi
mkdir -p $savedir

#asxtop100
#wget -O floatdatadownload/asx100.zip "http://float.com.au/download/asx_top_onehundred.zip?ticker=ABC,AGL,ALQ,AWC,AMC,AMP,ANN,ANZ,APA,ALL,ASX,ALX,AZJ,AST,BOQ,BEN,BHP,BSL,BLD,BXB,CTX,CAR,CGF,CHC,CIM,CWY,CCL,COH,CBA,CPU,CWN,CSL,CSR,CYB,DXS,DMP,DOW,DLX,EVN,FLT,FMG,GMG,GPT,GNC,HVN,HSO,ILU,IPL,IAG,IOF,IFL,JHX,JHG,JBH,LLC,LNK,MQG,MFG,MPL,MGR,NAB,NCM,NST,OSH,ORI,ORG,ORA,OZL,PDL,PPT,QAN,QBE,QUB,RHC,REA,RMD,RIO,STO,SCG,SEK,SHL,S32,SKI,SGP,SUN,SYD,TAH,TLS,A2M,SGR,TPM,TCL,TWE,VCX,WES,WFD,WBC,WPL,WOW,XRO"

#asxtop50
#wget -O floatdatadownload/asx50.zip "http://float.com.au/download/asx_top_onehundred.zip?ticker=AGL,AMC,AMP,ANZ,APA,ALL,ASX,AZJ,BHP,BXB,CTX,COH,COL,CBA,CPU,CSL,DXS,FMG,GMG,GPT,IAG,JHX,LLC,MQG,MPL,MGR,NAB,NCM,OSH,ORI,ORG,QAN,QBE,RHC,RIO,STO,SCG,SHL,S32,SGP,SUN,SYD,TLS,TCL,TWE,VCX,WES,WBC,WPL,WOW"

#per month
#wget -O floatdatadownload/201801.zip "http://float.com.au/download/201801.zip?ticker=ABC,AGL,ALQ,AWC,AMC,AMP,ANN,ANZ,APA,ALL,ASX,ALX,AZJ,AST,BOQ,BEN,BHP,BSL,BLD,BXB,CTX,CAR,CGF,CHC,CIM,CWY,CCL,COH,CBA,CPU,CWN,CSL,CSR,CYB,DXS,DMP,DOW,DLX,EVN,FLT,FMG,GMG,GPT,GNC,HVN,HSO,ILU,IPL,IAG,IOF,IFL,JHX,JHG,JBH,LLC,LNK,MQG,MFG,MPL,MGR,NAB,NCM,NST,OSH,ORI,ORG,ORA,OZL,PDL,PPT,QAN,QBE,QUB,RHC,REA,RMD,RIO,STO,SCG,SEK,SHL,S32,SKI,SGP,SUN,SYD,TAH,TLS,A2M,SGR,TPM,TCL,TWE,VCX,WES,WFD,WBC,WPL,WOW,XRO"
#wget -O floatdatadownload/201802.zip "http://float.com.au/download/201802.zip?ticker=ABC,AGL,ALQ,AWC,AMC,AMP,ANN,ANZ,APA,ALL,ASX,ALX,AZJ,AST,BOQ,BEN,BHP,BSL,BLD,BXB,CTX,CAR,CGF,CHC,CIM,CWY,CCL,COH,CBA,CPU,CWN,CSL,CSR,CYB,DXS,DMP,DOW,DLX,EVN,FLT,FMG,GMG,GPT,GNC,HVN,HSO,ILU,IPL,IAG,IOF,IFL,JHX,JHG,JBH,LLC,LNK,MQG,MFG,MPL,MGR,NAB,NCM,NST,OSH,ORI,ORG,ORA,OZL,PDL,PPT,QAN,QBE,QUB,RHC,REA,RMD,RIO,STO,SCG,SEK,SHL,S32,SKI,SGP,SUN,SYD,TAH,TLS,A2M,SGR,TPM,TCL,TWE,VCX,WES,WFD,WBC,WPL,WOW,XRO"
#wget -O floatdatadownload/201803.zip "http://float.com.au/download/201803.zip?ticker=ABC,AGL,ALQ,AWC,AMC,AMP,ANN,ANZ,APA,ALL,ASX,ALX,AZJ,AST,BOQ,BEN,BHP,BSL,BLD,BXB,CTX,CAR,CGF,CHC,CIM,CWY,CCL,COH,CBA,CPU,CWN,CSL,CSR,CYB,DXS,DMP,DOW,DLX,EVN,FLT,FMG,GMG,GPT,GNC,HVN,HSO,ILU,IPL,IAG,IOF,IFL,JHX,JHG,JBH,LLC,LNK,MQG,MFG,MPL,MGR,NAB,NCM,NST,OSH,ORI,ORG,ORA,OZL,PDL,PPT,QAN,QBE,QUB,RHC,REA,RMD,RIO,STO,SCG,SEK,SHL,S32,SKI,SGP,SUN,SYD,TAH,TLS,A2M,SGR,TPM,TCL,TWE,VCX,WES,WFD,WBC,WPL,WOW,XRO"
#wget -O floatdatadownload/201804.zip "http://float.com.au/download/201804.zip?ticker=ABC,AGL,ALQ,AWC,AMC,AMP,ANN,ANZ,APA,ALL,ASX,ALX,AZJ,AST,BOQ,BEN,BHP,BSL,BLD,BXB,CTX,CAR,CGF,CHC,CIM,CWY,CCL,COH,CBA,CPU,CWN,CSL,CSR,CYB,DXS,DMP,DOW,DLX,EVN,FLT,FMG,GMG,GPT,GNC,HVN,HSO,ILU,IPL,IAG,IOF,IFL,JHX,JHG,JBH,LLC,LNK,MQG,MFG,MPL,MGR,NAB,NCM,NST,OSH,ORI,ORG,ORA,OZL,PDL,PPT,QAN,QBE,QUB,RHC,REA,RMD,RIO,STO,SCG,SEK,SHL,S32,SKI,SGP,SUN,SYD,TAH,TLS,A2M,SGR,TPM,TCL,TWE,VCX,WES,WFD,WBC,WPL,WOW,XRO"
#wget -O floatdatadownload/201805.zip "http://float.com.au/download/201805.zip?ticker=ABC,AGL,ALQ,AWC,AMC,AMP,ANN,ANZ,APA,ALL,ASX,ALX,AZJ,AST,BOQ,BEN,BHP,BSL,BLD,BXB,CTX,CAR,CGF,CHC,CIM,CWY,CCL,COH,CBA,CPU,CWN,CSL,CSR,CYB,DXS,DMP,DOW,DLX,EVN,FLT,FMG,GMG,GPT,GNC,HVN,HSO,ILU,IPL,IAG,IOF,IFL,JHX,JHG,JBH,LLC,LNK,MQG,MFG,MPL,MGR,NAB,NCM,NST,OSH,ORI,ORG,ORA,OZL,PDL,PPT,QAN,QBE,QUB,RHC,REA,RMD,RIO,STO,SCG,SEK,SHL,S32,SKI,SGP,SUN,SYD,TAH,TLS,A2M,SGR,TPM,TCL,TWE,VCX,WES,WFD,WBC,WPL,WOW,XRO"

#wget -O floatdatadownload/2012.zip "http://float.com.au/download/2012.zip?ticker=GL,AMC,AMP,ANZ,APA,ALL,ASX,AZJ,BHP,BXB,CTX,COH,COL,CBA,CPU,CSL,DXS,FMG,GMG,GPT,IAG,JHX,LLC,MQG,MPL,MGR,NAB,NCM,OSH,ORI,ORG,QAN,QBE,RHC,RIO,STO,SCG,SHL,S32,SGP,SUN,SYD,TLS,TCL,TWE,VCX,WES,WBC,WPL,WOW"
#wget -O floatdatadownload/2013.zip "http://float.com.au/download/2013.zip?ticker=GL,AMC,AMP,ANZ,APA,ALL,ASX,AZJ,BHP,BXB,CTX,COH,COL,CBA,CPU,CSL,DXS,FMG,GMG,GPT,IAG,JHX,LLC,MQG,MPL,MGR,NAB,NCM,OSH,ORI,ORG,QAN,QBE,RHC,RIO,STO,SCG,SHL,S32,SGP,SUN,SYD,TLS,TCL,TWE,VCX,WES,WBC,WPL,WOW"
#wget -O floatdatadownload/2014.zip "http://float.com.au/download/2014.zip?ticker=GL,AMC,AMP,ANZ,APA,ALL,ASX,AZJ,BHP,BXB,CTX,COH,COL,CBA,CPU,CSL,DXS,FMG,GMG,GPT,IAG,JHX,LLC,MQG,MPL,MGR,NAB,NCM,OSH,ORI,ORG,QAN,QBE,RHC,RIO,STO,SCG,SHL,S32,SGP,SUN,SYD,TLS,TCL,TWE,VCX,WES,WBC,WPL,WOW"
#wget -O floatdatadownload/2015.zip "http://float.com.au/download/2015.zip?ticker=GL,AMC,AMP,ANZ,APA,ALL,ASX,AZJ,BHP,BXB,CTX,COH,COL,CBA,CPU,CSL,DXS,FMG,GMG,GPT,IAG,JHX,LLC,MQG,MPL,MGR,NAB,NCM,OSH,ORI,ORG,QAN,QBE,RHC,RIO,STO,SCG,SHL,S32,SGP,SUN,SYD,TLS,TCL,TWE,VCX,WES,WBC,WPL,WOW"
#wget -O floatdatadownload/2016.zip "http://float.com.au/download/2016.zip?ticker=GL,AMC,AMP,ANZ,APA,ALL,ASX,AZJ,BHP,BXB,CTX,COH,COL,CBA,CPU,CSL,DXS,FMG,GMG,GPT,IAG,JHX,LLC,MQG,MPL,MGR,NAB,NCM,OSH,ORI,ORG,QAN,QBE,RHC,RIO,STO,SCG,SHL,S32,SGP,SUN,SYD,TLS,TCL,TWE,VCX,WES,WBC,WPL,WOW"
#wget -O floatdatadownload/2017.zip "http://float.com.au/download/2017.zip?ticker=GL,AMC,AMP,ANZ,APA,ALL,ASX,AZJ,BHP,BXB,CTX,COH,COL,CBA,CPU,CSL,DXS,FMG,GMG,GPT,IAG,JHX,LLC,MQG,MPL,MGR,NAB,NCM,OSH,ORI,ORG,QAN,QBE,RHC,RIO,STO,SCG,SHL,S32,SGP,SUN,SYD,TLS,TCL,TWE,VCX,WES,WBC,WPL,WOW"
#wget -O floatdatadownload/2018.zip "http://float.com.au/download/2018.zip?ticker=GL,AMC,AMP,ANZ,APA,ALL,ASX,AZJ,BHP,BXB,CTX,COH,COL,CBA,CPU,CSL,DXS,FMG,GMG,GPT,IAG,JHX,LLC,MQG,MPL,MGR,NAB,NCM,OSH,ORI,ORG,QAN,QBE,RHC,RIO,STO,SCG,SHL,S32,SGP,SUN,SYD,TLS,TCL,TWE,VCX,WES,WBC,WPL,WOW"
#wget -O floatdatadownload/2019.zip "http://float.com.au/download/2019.zip?ticker=GL,AMC,AMP,ANZ,APA,ALL,ASX,AZJ,BHP,BXB,CTX,COH,COL,CBA,CPU,CSL,DXS,FMG,GMG,GPT,IAG,JHX,LLC,MQG,MPL,MGR,NAB,NCM,OSH,ORI,ORG,QAN,QBE,RHC,RIO,STO,SCG,SHL,S32,SGP,SUN,SYD,TLS,TCL,TWE,VCX,WES,WBC,WPL,WOW"

#https://www.asxhistoricaldata.com/
#https://www.marketindex.com.au/sites/default/files/historical-data/A2M.csv

pushd $savedir

unzip "*.zip"

cat ./*.txt > b.txt

#rm *.txt
popd
