import time
import alpaca_trade_api as tradeapi
from datetime import datetime



private_key = 'XQkERUV85BIDuwpyHGOfFgPIf0Mwh4pvKtmlnRZU'
public_key = 'PK7IMR8U59Y8N3ZPIV3W'
base_url = 'https://paper-api.alpaca.markets'
currentTicker = ''



all_stocks = ['AACI','AADI','AAL','AAON','AAPL','AATC','AAWW','ABCB','ABCL','ABCM','ABGI','ABMD','ABNB','ABOS','ABST','ABTX','ACAB','ACAD','ACAH','ACCD','ACET','ACGL','ACHC','ACHV','ACIU','ACIW','ACLS','ACMR','ACNB','ACQR','ACRS','ACT','ACTD','ACTG','ACVA','ADBE','ADER','ADES','ADI','ADP','ADPT','ADSK','ADTN','ADUS','ADV','AEAC','AEACU','AEAE','AEHA','AEIS','AEP','AEPPZ','AERI','AEYE','AFAC','AFAQ','AFCG','AFMD','AFRM','AFYA','AGGR','AGIO','AGNC','AGYS','AHCO','AHPA','AIMC','AINV','AIP','AIRG','AIRS','AKAM','AKIC','AKRO','AKTS','AKUS','AKYA','ALBO','ALCO','ALEC','ALGM','ALGN','ALGT','ALHC','ALIM','ALKS','ALKT','ALLO','ALNY','ALOR','ALORU','ALOT','ALPN','ALRM','ALRS','ALSA','ALT','ALTO','ALTR','ALTU','ALVR','ALXO','AMAL','AMAT','AMBA','AMCI','AMCX','AMD','AMED','AMEH','AMGN','AMKR','AMNB','AMOT','AMPH','AMRK','AMSC','AMSF','AMSWA','AMTB','AMTX','AMWD','AMYT','AMZN','ANAB','ANDE','ANGI','ANGO','ANIK','ANIP','ANSS','ANZU','ANZUU','AOSL','AOUT','APA','APAC','APEI','APEN','API','APLS','APOG','APP','APPF','APPN','APPS','APYX','ARBG','ARCB','ARCC','ARCE','ARCK','ARCT','ARGX','ARHS','ARIZ','ARIZU','ARKO','ARKR','ARLP','AROW','ARQT','ARRW','ARRY','ARTE','ARTNA','ARVN','ARWR','ASLE','ASML','ASND','ASO','ASPC','ASPS','ASRT','ASRV','ASTE','ASTL','ASUR','ASYS','ATAI','ATAK','ATAX','ATCX','ATEC','ATEX','ATHA','ATLC','ATLO','ATNI','ATOM','ATRA','ATRC','ATRI','ATRO','ATSG','ATVC','ATVI','ATXS','AUB','AUBN','AUDC','AUPH','AVAC','AVAV','AVDX','AVGO','AVHI','AVID','AVIR','AVNW','AVO','AVPT','AVT','AVXL','AXGN','AXNX','AXON','AXSM','AXTI','AY','AZ','AZN','AZPN','AZTA','BAFN','BAND','BANF','BANR','BANX','BASE','BATRA','BATRK','BBBY','BBCP','BBIO','BBQ','BBSI','BCAC','BCBP','BCML','BCOR','BCOV','BCOW','BCPC','BCRX','BCSA','BCYC','BEAM','BECN','BELFA','BELFB','BFC','BFIN','BFST','BGCP','BGNE','BHAC','BHF','BHSE','BIDU','BIGC','BIIB','BILI','BIOL','BIOS','BIOSU','BJRI','BKCC','BKEP','BKNG','BKR','BKSC','BL','BLBD','BLDE','BLDP','BLEU','BLFS','BLFY','BLI','BLKB','BLMN','BLSA','BLTS','BLU','BLZE','BMAQ','BMBL','BMEA','BMRC','BMRN','BNFT','BNNR','BNTX','BOCN','BOKF','BOOM','BOTJ','BPMC','BPOP','BPRN','BPYPO','BPYPP','BRIV','BRKH','BRKL','BRKR','BRLI','BRLT','BRP','BRY','BRZE','BSBK','BSET','BSGA','BSKY','BSKYU','BSRR','BSVN','BSY','BTAI','BTRS','BTWN','BUSE','BVS','BWAY','BWB','BWC','BWFG','BWMN','BWMX','BYRN','BZ','BZUN','CAC','CACC','CAKE','CALB','CALM','CAMP','CAMT','CAN','CAR','CARA','CARE','CARG','CASH','CASS','CASY','CATC','CATY','CBAN','CBFV','CBNK','CBRG','CBRL','CBSH','CBTX','CCAP','CCB','CCBG','CCCC','CCEL','CCEP','CCMP','CCNE','CCOI','CCRN','CCSI','CCTS','CD','CDAQ','CDEV','CDK','CDLX','CDMO','CDNA','CDNS','CDW','CDXS','CECE','CELC','CELH','CENT','CENTA','CENX','CERE','CERN','CERS','CERT','CEVA','CFB','CFBK','CFFI','CFFN','CFFS','CFIV','CFIVU','CFLT','CFRX','CG','CGBD','CGEM','CGNT','CGNX','CHCO','CHDN','CHEF','CHK','CHKP','CHMG','CHNG','CHRS','CHRW','CHTR','CHUY','CHX','CIGI','CIIG','CINF','CITE','CITEU','CIVB','CIZN','CLAQ','CLAR','CLBK','CLDX','CLFD','CLIN','CLINU','CLLS','CLMT','CLNE','CLOE','CLPT','CLRM','CLST','CMAX','CMBM','CMCA','CMCO','CMCSA','CMCT','CME','CMLS','CMPR','CMPS','CMTL','CNDT','CNOB','CNSL','CNTA','CNTQ','CNTY','CNXC','CNXN','COCO','CODA','CODX','COFS','COGT','COHR','COHU','COIN','COKE','COLB','COLI','COLL','COLM','COMM','CONN','CONX','COOL','COOP','CORT','COST','COUP','COVA','COVAU','COWN','CPAA','CPAR','CPARU','CPHC','CPLP','CPRT','CPRX','CPSI','CPSS','CRAI','CRBU','CRDO','CREC','CRECU','CRMD','CRMT','CRNC','CRNX','CROX','CRSP','CRSR','CRTO','CRUS','CRVL','CRWD','CRWS','CSBR','CSCO','CSGP','CSGS','CSII','CSIQ','CSPI','CSTE','CSTL','CSTR','CSWC','CSWI','CSX','CTAQ','CTAQU','CTAS','CTBI','CTG','CTKB','CTLP','CTRE','CTRN','CTSH','CTXS','CUBA','CUE','CULL','CUTR','CVBF','CVCO','CVCY','CVET','CVGI','CVGW','CVLG','CVLT','CVLY','CVRX','CVV','CWBC','CWCO','CWST','CYBE','CYBR','CYRX','CYTK','CZNC','CZR','CZWI','DADA','DAIO','DAKT','DALN','DAOO','DAWN','DBX','DCBO','DCGO','DCOM','DCOMP','DCPH','DCRD','DCT','DENN','DFFN','DFH','DGICA','DGICB','DGII','DGNU','DH','DHBC','DHCA','DHHC','DHIL','DIBS','DICE','DIOD','DISAU','DISH','DJCO','DKDCA','DKNG','DLCAU','DLHC','DLO','DLTH','DLTR','DMAQ','DMRC','DMTK','DNAA','DNAB','DNAC','DNAD','DNLI','DNUT','DOCU','DOMO','DOOO','DORM','DOX','DPCS','DRAY','DRIO','DRVN','DSAC','DSEY','DSGN','DSGX','DSKE','DSP','DTOC','DUNE','DUOL','DVAX','DXCM','DXLG','DXPE','DYN','DZSI','EA','EBAY','EBC','EBIX','EBMT','EBTC','ECPG','EDIT','EDNC','EDRY','EDTX','EDUC','EEFT','EFSC','EGAN','EGBN','EGLE','EGRX','EHTH','EIGR','EMKR','EML','ENER','ENPH','ENSG','ENTA','ENTF','ENTG','ENVX','EOLS','EPHY','EPIX','EPSN','EQBK','EQIX','EQRX','ERAS','ERES','ERIC','ERIE','ERII','ESAC','ESCA','ESGR','ESLT','ESPR','ESQ','ESSA','ESTA','ETAC','ETSY','EUCR','EVBG','EVCM','EVER','EVLV','EVO','EVOJ','EVOP','EWBC','EWCZ','EWTX','EXAS','EXC','EXEL','EXLS','EXPD','EXPE','EXPI','EXPO','EXTR','EYE','EZPW','FA','FANG','FANH','FARM','FARO','FAST','FATE','FATP','FB','FBIZ','FBMS','FBNC','FCBC','FCCO','FCEL','FCFS','FCNCA','FCRD','FDBC','FDMT','FDUS','FEAM','FEIM','FELE','FENC','FFBC','FFBW','FFIC','FFIN','FFIV','FFNW','FFWM','FGBI','FGEN','FGMC','FGMCU','FHB','FHTX','FIAC','FIACU','FIBK','FINM','FINMU','FINW','FISI','FISV','FITB','FIVE','FIVN','FIZZ','FKWL','FLAC','FLEX','FLGT','FLIC','FLL','FLMN','FLNC','FLWS','FLXS','FLYW','FMAO','FMBH','FMNB','FMTX','FNCB','FNKO','FNLC','FNVT','FNWB','FOCS','FOLD','FONR','FORA','FORM','FORR','FOSL','FOX','FOXA','FOXF','FOXW','FRAF','FRBA','FRBK','FREE','FRG','FRGI','FRLA','FRME','FROG','FRON','FRONU','FRPH','FRPT','FRSG','FRSH','FRST','FRWAU','FSBC','FSBW','FSFG','FSLR','FSRX','FSRXU','FSSI','FSTR','FSV','FTAA','FTAI','FTCI','FTCV','FTDR','FTHM','FTNT','FTPA','FULT','FUNC','FUSB','FUTU','FVAM','FVCB','FWAC','FWONA','FWONK','FWRD','FWRG','FXNC','FYBR','GABC','GACQ','GAIA','GAIN','GAN','GATE','GBDC','GBIO','GBNY','GBRG','GBT','GDEN','GDNR','GDRX','GDS','GDYN','GENC','GEVO','GFS','GGAA','GGAL','GGMC','GH','GHAC','GHIX','GIFI','GIII','GIIX','GILD','GIW','GLAD','GLAQ','GLBE','GLBL','GLDD','GLEE','GLHA','GLNG','GLPG','GLPI','GLRE','GLUE','GMAB','GMFI','GMGI','GNAC','GNSS','GNTX','GNTY','GO','GOGL','GOOD','GOOG','GOOGL','GOSS','GPAC','GPACU','GPP','GPRE','GPRO','GRCL','GRFS','GRIN','GROW','GRPN','GRVY','GRWG','GSAQ','GSBC','GSEV','GSHD','GSIT','GSM','GSRM','GSRMU','GT','GTAC','GTACU','GTHX','GTIM','GTLB','GTPA','GTPB','GTX','GTXAP','GTYH','GURE','GVCI','GWRS','HA','HAAC','HAFC','HAIN','HALO','HAS','HAYN','HBAN','HBCP','HBIO','HBNC','HBT','HCAR','HCAT','HCCI','HCIC','HCII','HCKT','HCM','HCMA','HCNE','HCSG','HCVI','HCVIU','HDSN','HEAR','HEES','HELE','HERA','HERAU','HFFG','HFWA','HHS','HIBB','HIFS','HIII','HIIIU','HIMX','HIVE','HLAH','HLAHU','HLIT','HLMN','HLNE','HMCO','HMNF','HMST','HMTV','HNNA','HNRG','HNST','HOFT','HOLI','HOLX','HON','HONE','HOPE','HPLT','HQI','HQY','HRMY','HRTX','HRZN','HSAQ','HSIC','HSII','HSKA','HSON','HST','HSTM','HTBI','HTBK','HTHT','HTLD','HTLF','HTLFP','HTZ','HUBG','HURC','HURN','HWBK','HWC','HWEL','HWKN','HYFM','HYZN','HZNP','IAC','IART','IAS','IBCP','IBEX','IBKR','IBOC','IBRX','IBTX','ICAD','ICCC','ICFI','ICHR','ICLR','ICMB','ICPT','ICUI','ICVX','IDCC','IDXX','IDYA','IEA','IEP','IESC','IGAC','IGIC','IGMS','IGNY','IHRT','III','IIII','IIIV','IIVI','IKNA','ILMN','ILPT','IMAQ','IMCR','IMGN','IMGO','IMKTA','IMMR','IMOS','IMRX','IMUX','IMVT','IMXI','INBK','INBX','INCY','INDB','INDT','INFN','INGN','INKA','INMB','INMD','INOD','INSE','INSM','INTA','INTC','INTE','INTU','INVA','INVE','INVZ','IOAC','IONS','IOSP','IOVA','IPAR','IPAX','IPGP','IPSC','IPVIU','IQ','IQMD','IRBT','IRDM','IRMD','IROQ','IRTC','IRWD','ISAA','ISEE','ISLE','ISRG','ISSC','ISTR','ITAQ','ITCI','ITHX','ITIC','ITOS','ITQ','ITRI','ITRN','IVAC','IVCB','IVCP','JACK','JAKK','JAMF','JANX','JAQC','JAZZ','JBHT','JBLU','JBSS','JCIC','JCICU','JD','JGGC','JGGCU','JJSF','JKHY','JMAC','JNCE','JOFF','JOFFU','JOUT','JRVR','JUGG','JUGGU','JWAC','JYAC','JYNT','KAII','KAIIU','KAIR','KAIRU','KALU','KALV','KARO','KBAL','KDNY','KDP','KE','KELYA','KEQU','KFFB','KFRC','KHC','KIDS','KIIIU','KINS','KINZ','KINZU','KLAC','KLAQ','KLIC','KLXE','KMPH','KNBE','KNSA','KNTE','KOD','KPTI','KRNL','KRNT','KRNY','KRON','KROS','KRT','KRTX','KRUS','KRYS','KSPN','KTCC','KTOS','KURA','KVHI','KVSA','KVSC','KYMR','KZIA','KZR','LAKE','LAMR','LANC','LAND','LARK','LASR','LATG','LAUR','LAX','LAZY','LBAI','LBC','LBPH','LBRDA','LBRDK','LBTYA','LBTYK','LCA','LCAA','LCNB','LCUT','LE','LECO','LEE','LEGA','LEGH','LEGN','LESL','LFAC','LFUS','LFVN','LGAC','LGACU','LGIH','LGND','LGO','LGST','LGSTU','LGTO','LGVC','LHCG','LI','LIBY','LIDR','LILA','LILAK','LINC','LIND','LION','LITE','LITT','LIVN','LJAQ','LJPC','LKFN','LKQ','LLNW','LMACA','LMACU','LMAT','LMNR','LMST','LNDC','LNSR','LNT','LNTH','LOB','LOCO','LOGI','LOOP','LOPE','LOVE','LPLA','LPRO','LPSN','LQDA','LQDT','LRCX','LRFC','LSBK','LSCC','LSEA','LSTR','LSXMA','LSXMK','LTRN','LTRX','LULU','LUMO','LUNA','LUNG','LVRA','LWAY','LYEL','LYFT','LYLT','LYTS','MACA','MACK','MANH','MANT','MAPS','MAQC','MAR','MASI','MASS','MAT','MATW','MAXN','MBCN','MBIN','MBTC','MBTCU','MBUU','MBWM','MCAA','MCAAU','MCAE','MCAF','MCBC','MCBS','MCFT','MCHP','MCRB','MCRI','MDB','MDGL','MDLZ','MDRX','MDWT','MDXG','MEAC','MEDP','MEKA','MELI','MEOH','MERC','METC','MFIN','MGEE','MGI','MGIC','MGNI','MGNX','MGPI','MGRC','MGTX','MGYR','MIDD','MIRM','MITA','MITK','MKSI','MKTX','MLAB','MLAI','MLCO','MLKN','MLVF','MMSI','MMYT','MNDT','MNDY','MNKD','MNRO','MNSB','MNST','MNTK','MNTV','MNTX','MODV','MOFG','MOMO','MON','MONCU','MORF','MORN','MPAA','MPB','MPRA','MPWR','MQ','MRAM','MRBK','MRCC','MRCY','MRNA','MRNS','MRSN','MRTN','MRTX','MRUS','MRVI','MRVL','MSAC','MSBI','MSDA','MSDAU','MSEX','MSFT','MSVB','MTBC','MTCH','MTEX','MTLS','MTRX','MTRY','MTSI','MTTR','MU','MUDS','MVBF','MXCT','MXL','MYFW','MYGN','MYPS','MYRG','NAII','NARI','NATH','NATI','NATR','NAUT','NAVI','NBIX','NBN','NBST','NBTB','NCAC','NCNO','NCSM','NDAC','NDAQ','NDLS','NDSN','NECB','NEO','NEOG','NESR','NEWT','NFBK','NFE','NFLX','NGM','NGMS','NHIC','NHTC','NICE','NICK','NIU','NKSH','NKTR','NLOK','NMFC','NMIH','NMMC','NMRK','NOAC','NODK','NOTV','NOVT','NPCE','NRAC','NRACU','NRC','NRIM','NRIX','NSIT','NSSC','NSTG','NTAP','NTCT','NTES','NTGR','NTIC','NTLA','NTNX','NTRA','NTRS','NTUS','NTWK','NUVA','NUVL','NVAX','NVCR','NVDA','NVEC','NVEE','NVEI','NVMI','NVSA','NVSAU','NVTS','NWBI','NWE','NWFL','NWL','NWLI','NWPX','NWS','NWSA','NXGN','NXPI','NXST','NXTC','NYMT','OAS','OB','OBNK','OCAX','OCC','OCFC','OCSL','OCUL','ODFL','ODP','OEPW','OEPWU','OFIX','OFLX','OFS','OHPA','OHPAU','OIIM','OKTA','OLED','OLK','OLLI','OLPX','OM','OMAB','OMCL','OMEG','OMIC','ON','ONB','ONDS','ONEM','ONEW','ONYX','OPBK','OPCH','OPEN','OPHC','OPI','OPNT','OPOF','OPRT','OPRX','OPT','ORGN','ORGO','ORLY','ORMP','ORRF','OSBC','OSIS','OSPN','OSTK','OSTR','OSUR','OSW','OTEC','OTEX','OTLY','OTTR','OVBC','OVLY','OXAC','OXLC','OXSQ','OXUS','OYST','OZK','PAA','PACB','PACW','PACX','PAGP','PAHC','PANL','PANW','PAQC','PAQCU','PARA','PARAA','PATI','PATK','PAX','PAYA','PAYO','PAYX','PBAX','PBFS','PBHC','PBIP','PBPB','PCAR','PCB','PCCT','PCH','PCRX','PCSB','PCT','PCTI','PCTY','PCVX','PCX','PCYG','PCYO','PDCE','PDCO','PDD','PDEX','PDFS','PDLB','PDSB','PEBK','PEBO','PECO','PEGA','PENN','PEP','PEPL','PERI','PESI','PETQ','PETS','PFBC','PFC','PFDR','PFG','PFHD','PFIN','PFIS','PFSW','PGC','PGNY','PGRW','PHAT','PHIC','PI','PINC','PKBK','PKOH','PLAB','PLAY','PLBC','PLBY','PLCE','PLL','PLMI','PLPC','PLRX','PLTK','PLUG','PLUS','PLXS','PLYA','PMD','PMGM','PMGMU','PMTS','PMVP','PNFP','PNT','PNTG','PODD','PONO','POOL','POSH','POW','POWI','POWL','POWRU','POWW','PPBI','PPC','PPHP','PPIH','PPTA','PPYA','PRAA','PRAX','PRCH','PRDO','PRFT','PRGS','PRIM','PRLD','PROV','PRPH','PRPL','PRSR','PRTA','PRTS','PRVA','PRVB','PSAG','PSEC','PSMT','PSNL','PTC','PTCT','PTEN','PTGX','PTIC','PTICU','PTOC','PTON','PTRA','PTSI','PTVE','PUBM','PUCK','PVBC','PWOD','PWP','PWUP','PYCR','PYPL','PZZA','QCOM','QCRH','QDEL','QFIN','QLYS','QNST','QRHC','QRTEA','QRTEP','QRVO','QTRX','QUIK','QURE','RADA','RADI','RAIL','RAPT','RARE','RBB','RBCAA','RCEL','RCHG','RCII','RCKT','RCKY','RCLF','RCM','RCMT','RDCM','RDFN','RDI','RDNT','RDUS','RDVT','RDWR','REG','REGI','REGN','RELL','RELY','REPL','RETA','REVE','REVH','REVHU','REYN','RGCO','RGEN','RGLD','RGNX','RGP','RICK','RILY','RIOT','RKLB','RLAY','RLMD','RLYB','RMBI','RMBS','RMGC','RMR','RNA','RNDB','RNLX','RNST','RNW','ROAD','ROC','ROCC','ROCG','ROCK','ROCL','ROIC','ROKU','ROLL','ROSE','ROST','ROVR','RPAY','RPD','RPID','RPRX','RPTX','RRBI','RRGB','RRR','RSVR','RTL','RTLR','RUN','RUSHA','RUSHB','RUTH','RVAC','RVMD','RVNC','RVSB','RWAY','RXDX','RXRX','RXST','RXT','RYAAY','RYTM','SABR','SAFM','SAFT','SAGA','SAGE','SAIA','SAL','SAMG','SANA','SANB','SANG','SANM','SASR','SATS','SBAC','SBCF','SBFG','SBGI','SBLK','SBNY','SBRA','SBSI','SBT','SBTX','SBUX','SCHL','SCHN','SCLE','SCOA','SCOB','SCOBU','SCPH','SCPL','SCRM','SCSC','SCVL','SCWX','SDAC','SDACU','SDGR','SEAT','SEDG','SEER','SEIC','SELF','SENEA','SFBC','SFIX','SFM','SFNC','SFST','SGA','SGC','SGEN','SGH','SGHT','SGII','SGMO','SGRY','SHBI','SHC','SHCA','SHEN','SHLS','SHOO','SHQA','SHUAU','SHYF','SIBN','SIER','SIGA','SIGI','SILC','SILK','SIMO','SITM','SIVB','SKIN','SKYT','SKYW','SLAB','SLAM','SLCR','SLGC','SLGN','SLM','SLNG','SLP','SLRC','SLVR','SMBC','SMBK','SMCI','SMED','SMIH','SMIHU','SMLR','SMMF','SMPL','SMTC','SMTI','SNBR','SNCE','SNCY','SND','SNDX','SNEX','SNFCA','SNPO','SNPS','SNRH','SNY','SOFI','SOHU','SONO','SOPH','SOTK','SOVO','SP','SPFI','SPK','SPLK','SPNE','SPNS','SPOK','SPSC','SPT','SPTK','SPTN','SPWH','SPWR','SQFT','SRAX','SRCE','SRCL','SRDX','SRGA','SRPT','SRRK','SRTS','SSAA','SSB','SSBI','SSNC','SSP','SSRM','SSSS','SSTI','SSYS','STAA','STBA','STEP','STER','STGW','STKL','STKS','STLD','STNE','STOK','STRA','STRL','STRO','STRS','STRT','STSA','STX','SUMO','SUPN','SVC','SVFA','SVFAU','SVFB','SVFC','SVNA','SVNAU','SWAG','SWAV','SWBI','SWET','SWIM','SWIR','SWKH','SWKS','SWSS','SWTX','SYBT','SYNA','SYNH','SYNL','TA','TACT','TAIT','TALS','TARA','TARS','TASK','TBBK','TBCP','TBCPU','TBK','TBLA','TBNK','TBPH','TCBC','TCBI','TCBK','TCDA','TCFC','TCMD','TCOM','TCPC','TCRX','TCVA','TCX','TDUP','TEAM','TECH','TEDU','TEKK','TELA','TENB','TER','TESS','TETC','TETCU','TFFP','TFSL','TGA','TGAA','TGAAU','TGLS','TGTX','TGVC','TH','THAC','THCP','THFF','THRM','THRN','THRY','TIG','TIL','TILE','TIOA','TIOAU','TIPT','TITN','TKNO','TLGY','TLS','TMCI','TMDX','TMPM','TMUS','TNDM','TNGX','TNYA','TOWN','TPG','TPIC','TPTX','TREE','TRHC','TRIN','TRIP','TRMB','TRMD','TRMK','TRMR','TRNS','TRON','TROW','TRS','TRST','TRUE','TRUP','TSBK','TSCO','TSEM','TSIB','TSIBU','TSLA','TSP','TTD','TTEC','TTEK','TTGT','TTMI','TTSH','TTWO','TVTX','TVTY','TW','TWCB','TWIN','TWKS','TWLV','TWNK','TWOU','TWST','TXN','TXRH','TZOO','TZPS','UAL','UBCP','UBFO','UBOH','UBSI','UCBI','UCTT','UDMY','UEIC','UFCS','UFPI','UFPT','UG','UHAL','UK','ULBI','ULCC','ULH','ULTA','UMBF','UMPQ','UNIT','UNTY','UPLD','UPTD','UPWK','URBN','URGN','USAK','USAP','USCB','USLM','UTAA','UTHR','UTMD','UVSP','VABK','VALU','VAQC','VBNK','VBOC','VBTX','VC','VCEL','VCSA','VCTR','VCXA','VCYT','VECO','VECT','VERA','VERI','VERV','VERX','VFF','VG','VIA','VIAV','VICR','VII','VINP','VIR','VIRC','VIRI','VIRT','VITL','VIVO','VLAT','VLGEA','VLY','VMCA','VMD','VMEO','VMGA','VNDA','VNET','VNOM','VOD','VOR','VOXX','VPCB','VRA','VRDN','VREX','VRNA','VRNS','VRNT','VRRM','VRSK','VRSN','VRTS','VRTX','VSAC','VSAT','VSEC','VSTA','VTAQ','VTIQ','VTRS','VTSI','VWE','VXRT','VYGR','WABC','WAFD','WALD','WASH','WAVS','WB','WBA','WBD','WDAY','WDC','WDFC','WEN','WERN','WETF','WEYS','WFRD','WHF','WHLRP','WINA','WING','WIRE','WIX','WKME','WLDN','WLFC','WMG','WMPN','WNEB','WOOF','WRLD','WSBC','WSBF','WSC','WSFS','WSTG','WTBA','WTFC','WTW','WVVI','WW','WWD','WYNN','XAIR','XBIT','XEL','XENE','XFINU','XGN','XM','XNCR','XOMA','XP','XPAX','XPAXU','XPDBU','XPEL','XPER','XRAY','XRX','YELL','YMAB','YORW','YY','Z','ZBRA','ZD','ZEUS','ZG','ZI','ZION','ZLAB','ZM','ZNTL','ZS','ZUMZ','ZYXI']
Oldest ={}
Old ={}
New ={}
Newest ={}
num = 0


def findChar(Stock):
    l = 0
    value = ''
    charList = ['c', 'h', 'l', 'o']
    charNum = 0
    values = {}
    for i in range(len(Stock)):
        if Stock[i] == charList[charNum]:
            j = i+4
            l = priceLen(j, Stock)
        if l > 0:
            value += str(Stock[i+4])
            l -= 1
        if not value == '' and l == 0:
            values[charList[charNum]] = float(value)
            value = ''
            if(charNum < len(charList)-1):
                charNum += 1
    values['adjlow'] = 0
    values['adjopen'] = 0
    values['adjclose'] = 0
    values['adjhigh'] = 0
    return values


def priceLen(i, Stock):
    for j in range(i, len(Stock)):
        if Stock[j] == ',':
            return j-i









def get_all_values(nested_dictionary, old, currentTicker, Old, Oldest):
    c = -1
    h = -1
    l = -1
    n = -1
    num = 0
    for key, value in nested_dictionary.items():
        if type(value) is dict:
            currentTicker = key
            get_all_values(value, old, currentTicker, Old, Oldest)
        else:
            #print(old)
            if num == 3:
                n = value
                num += 1
            if num == 4 and not len(old) == 0:
                #The problem is that the ticker AGGR is in the stock list but was not defined for the first list them for the third list it was for some reason defined we need to remove those that dont return a value from the list in the list creation funtion 
                dic = toTheBottom(old[currentTicker])
                nested_dictionary['adjopen'] = (dic['o']+dic['c'])/2
                nested_dictionary['adjlow'] = (l)
                nested_dictionary['adjhigh'] = (h)
                nested_dictionary['adjclose'] = (h+n+c+l)/4
                WhatToDo(Oldest, Old, old, nested_dictionary, currentTicker)
                num += 1    
            if num == 2:
                l = value
                num += 1
            if num == 1:
                h = value
                num += 1 
            if num == 0:
                c = value
                num += 1
            

def toTheBottom(dic):
    for key, value in dic.items():
        if type(value) is dict:
            toTheBottom(value)
        else:
            return dic


def createStockList(all_stocks):

    

    stock_data = {}
    full_List = {}
    stock_data.clear()
    full_List.clear()
    api = tradeapi.REST(public_key, private_key, base_url)
    for stocks in all_stocks:
        t = api.get_bars(stocks, '1Hour', limit=1)
        if not t == []:
            stock_data[stocks] = t
        else:
            all_stocks.remove(stocks)
    for stocks in stock_data:
        full_List[stocks] = findChar(str(stock_data[stocks]))
    return full_List

def WhatToDo(Os, Ol, N, Ns, currentTicker):
    if not len(Os) == 0:
        api = tradeapi.REST(public_key, private_key, base_url)
        Oldest = toTheBottom(Os[currentTicker])
        Old = toTheBottom(Ol[currentTicker])
        New = toTheBottom(N[currentTicker])
        Newest = Ns
        print(Oldest)
        print('\n')
        print(Old)
        print('\n')
        print(New)
        print('\n')
        print(Newest)
        print('\n')
        if Oldest['adjopen'] > Oldest['adjclose'] and Old['adjopen'] > Old['adjclose'] and New['adjopen'] > New['adjclose'] and Newest['adjopen'] < Newest['adjclose']:
            q = int(5000/Newest['adjclose'])
            try:
                api.submit_order(symbol=currentTicker, qty=q, side='buy', type='market', time_in_force='day')
                print('Bought ' + currentTicker)
            except:
                print(currentTicker + ' cannot be bought')
        if Oldest['adjopen'] < Oldest['adjclose'] and Old['adjopen'] < Old['adjclose'] and New['adjopen'] < New['adjclose'] and Newest['adjopen'] > Newest['adjclose']:
            q = int(5000/Newest['adjclose'])
            try:
                api.submit_order(symbol=currentTicker, qty=q, side='sell', type='market', time_in_force='day')
                print('Shorted/Sold ' + currentTicker)
            except:
                print(currentTicker + ' cannot be shorted')
        
while True:
    if((datetime.now().hour>=9)and (datetime.now().hour<=13)):
        Oldest.clear()
        Oldest.update(Old)
        Old.clear()
        Old.update(New)
        New.clear()
        New.update(Newest)
        print(New)
        Newest.clear()
        Newest.update(createStockList(all_stocks))
        print(Newest)
        get_all_values(Newest, New, currentTicker, Old, Oldest)
        print('Loop')
        time.sleep(2400)
    else:
        time.sleep(60)



