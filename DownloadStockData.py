import urllib

NYSE_STOCKS = "DDD MMM WBAI WUBA AHC ATEN AAC AIR AAN ABB ABT ABBV ANF GCH JEQ SGF ABM AKR ACN ACCO ACW ATV ATU AYI ADX PEO AGRO ADPT ADT AAP WMS ASX AAV ATE AVK AGC LCM ACM ANW AEB AED AEG AEH AEK AER HIVE AJRD ARO AET AMG MGR AFL AFSD MITT MITT^A MITT^B AGCO A GAS AEM ADC GRO AGU AL APD AYR ARG AKS ALP^O ALG AGI ALK AIN ALB AA AA^B ALR ALR^B ALEX ALX ARE ARE^D ARE^E BABA Y ATI ALLE AGN AGN^A ALE AKP ADS AFB AOI AWF AB ACG LNT NCV NCZ ACV NIE NFJ AWH ALSN ALL ALL^A ALL^B ALL^C ALL^D ALL^E ALL^F ALLY ALLY^A ALLY^B BSI ALJ ALDW AGD AWP AOD RESI MO ACH AMBR ABEV AMC AMFW AEE AMRC AMX AAT AXL ACC AEO AEP AEL AXP AFA AFG AFGE AFGH AFW AMH AMH^A AMH^B AMH^C AIG AIG.WS AMID ARL AWR AMT AMT^A AMT^B AVD AWK APU AMP ABC ANFI AHS AP APH BETR AXR AME AFSI^A AFSI^B AFSI^C AFSI^D AFSI^E AFSS AFST AEUA APC AU BUD AXE NLY NLY^A NLY^C NLY^D AM AR ANTM ANTX ANH ANH^A ANH^B ANH^C AON APA AIV AIV^A AIV^Z ARI ARI^A APO AIB AIY AMTG AMTG^A AFT AIF APLE AIT ATR WTR ARMK ABR ABR^A ABR^B ABR^C ABRN ARC ARCX MT ARH^C ADM AROC ARCO ASC AFC ARU ACRE ARDC ARES AGX ANET AI AIC AIW AHH ARR ARR^A ARR^B AFI AWI ARW AJG APAM ASA ABG AHP AHT AHT^A AHT^D AHT^E ASH APB GRR ASPN AHL AHL^A AHL^B AHL^C ASB ASB^B ASB^C AC AIZ AGO AGO^B AGO^E AGO^F AF AF^C AZN T ATTO AT ARP ARP^D ARP^E ATO ATW AUO ATHM ALV AN AZO AVB AGR ACP AVY AVG AVH AVA AV AVV AVT AVP AVX AXTA AXLL AXS AXS^C AXS^D AZUR AZZ BGS BW MCI BGH MPV BMI BHI BBN BLL BGE^B BANC BANC^C BANC^D BANC^E BOCA.CL BBVA BBD BBDO BCH BLX BSBR BSAC SAN SAN^A SAN^B SAN^C SAN^I CIB BXS BAC BAC.WS.A BAC.WS.B BAC^C BAC^D BAC^E BAC^I BAC^L BAC^W BAC^Y BAC^Z BML^G BML^H BML^I BML^J BML^L BOH BMO BK BK^C BNS RATE BKU BCS BCS^ BCS^A BCS^C BCS^D BNED BKS B CUDA ABX BAS BXLT BAX BTE BBT BBT^D BBT^E BBT^F BBT^G BBT^H BFR BBX BCE BZH BDX BDC BXE BEL BMS BHE BRK.A BRK.B BHLB BBY BGCA BHP BBL BIG BH BBG BIOA BIOA.WS BIO BIO.B BITA BKH BKHU BKFS BSM BJZ BFZ CII BHK HYT BTZ DSU BHL BGR BDJ EGF FRA BFO BGT BOE BME BAF BKT BGY BKN BTA BIT MUI MNE MUA BPK BKK BIE BBK BBF BYM BFK BTT MEN MUC MUH MHD MFL MUJ MHN MUE MUS MVT MYC MCA MYD MYF MFT MIY MYJ MYN MPA MQT MYI MQY BNJ BNY BLH BQH BSE BCX BST BSD BUI BLK BGB BGX BSL BCRH BXC BWP BA BCC BCEI BOOT BAH BWA SAM BXP BXP^B BSX BOX BYD BP BPT BERY BRC BDN^E BDN LND BAK BRFS BPI BGG BFAM EAT BCO BMY BRS BRX BR BKD BAM BOXC DTLA^ INF HHY BIP BOI BPY BEP HTR BRO BF.A BF.B BRT BC BT BPL BKE BVN BBW BG BURL BWXT CJES BCR BNK GYB PFH CAB CABO CVC CBT COG CACI CAE CAI CAA CAL CCC CRC CWT CALX ELY CPE CPE^A CPN CBM CPT CCJ CPB CM CNI CNQ CP CAJ CMN COF COF.WS COF^C COF^D COF^F COF^P CSU BXMT CLA CMO CMO^E CRR CAH CCP CRCM CSL KMX CCL CUK CRS CSV CRI CSH CAS CSLT CTLT CTT CAT CATO CBZ CBL CBL^D CBL^E CBO IGR CBG CBS CBS.A CBX CDI CEB FUN CDR CDR^B CGI CE CLS CEL CPAC CX CNCO CVE CNC CEN CNP EBR EBR.B CEE CCS CTL CVO CF CGG GIB ECOM CRL CLDT CKP CMCM CHGG CHE CC CHMT CHMI CHK CHK^D CHKR CHSP CHSP^A CPK CVX CBI CHS CIM CO STV DL CEA CHN CGA LFC MY CHL NPD BORN SNP ZNH CHA CHU XNY CYD ZX CMG CHH CBK CHT CHD CBR CIEN CI XEC CBB CBB^B CNK CINR CIR CIT BLW C C.WS.A C^C C^J C^K C^L C^N C^P C^S CFG CIA CIO CVEO CIVI CLC CWEI CLH CCO CBA CEM EMO CTR CLW CNL CLF CLX CLD MYCC CMS CMS^B CNA CNHI CNO CEO CNXC COH CIE KOF KO CCE CDE FOF INB UTF LDP MIE RQI RNP PSF RFI CNS CFX CL CXE CIF CXH CMU CLNY CLNY^A CLNY^B CLNY^C SFR CPGX CPPL CXP STK CCV CCZ CMA CMA.WS FIX CMC CBU CYH CHCT CIG CIG.C CBD SBS ELP CCU CODI CMP CSC CRK CAG CXO CCM CNNX COP CNX ED STZ STZ.B CSTM TCS CBPX CLR VLRS CVG COO CTB CPS CPA CLB CLGX CORR CORR^A COR COR^A GLW GYC OFC OFC^L CXW CZZ CMRE CMRE^B CMRE^C CMRE^D COT COTY CCSC CFC^A CFC^B CUZ CVA CPF CPL CR CRD.A CRD.B BAP CS CPG CEQP CRH CRT CAPL CCI CCI^A CCK CRY CSRA CSS CST CTS CUBE CUBE^A CUB CFR CFR^A CFI CMI CW SRF SZC CUBI CUBI^C CUBI^D CUBS CSI CVT CVI UAN CVRR CVS CELP CYS CYS^A CYS^B DHI CB DAN DHR DAC DQ DRI DAR DVA DPM DCT DDR DDR^J DDR^K DF DECK DE DEX DDF DKL DK DLPH DAL DEL DLX DMD DWRE DNR DKT DB DTK DXB DVN DV DHX DHT DEO DO DRII DRH DSX DSX^B DSXN DKS DBD DLR DLR^E DLR^F DLR^G DLR^H DLR^I DGI DDS DDT DIN DPLO DFS DFS^B DRA DNI DLB DG DDC DM D DCUB DCUC DPZ UFS DCI LPG DSL DBL PLOW DEI DOV DDE DVD DOW DPS RDY DRD DW DHF DMB DSM LEO DRQ DST DSW DTE DTQ DTZ DCO DPG DSE DNP DTF DUC DUK DUKH DRE DNB DFT DFT^A DFT^B DHG DY DLNG DLNG^A DYN DYN.WS DYN^A DX DX^A DX^B DD DD^A DD^B SSP EGIF EXP ECC ECCA ECCZ DEA EGP EMN KODK KODK.WS KODK.WS.A ETN ETV ETW EV EOI EOS EFT EFF ETX EOT EVN ETJ EFR EVF EVG EVT ETO EXD ETG ETB ETY EXG ECT ECR ECL DANG EC EIX EDR EW EHIC EJ EP^C EE EGO LLY ELLI EFC EARN AKO.A AKO.B ERJ EMC EME EMES EBS EMG EMR EDE ESRT EIG EDN EOC ICA ENBL EEQ EEP ENB ECA EXK GI ENH ENH^B ENH^C NDRO EGN ENR EPC ETE ETP ERF ENI ENS EGL E ENLK ENLC EBF ENVA NPO ESV ETM EAA EAB EAE ETR ELA ELB ELJ ELU EFM EMQ EMZ ENJ ENO EZT EPD EVC ENV EVHC EVA ENZ EOG EPE EPAM EPR EPR^C EPR^E EPR^F EQT EQGP EQM EFX EQC EQC^D EQCO ELS ELS^C EQY EQR EQS ERA EROS ESE ESNT ESS ESS^H.CL EL ESL DEG ETH EURN EEA EVER EVER^A EVR RE EVRI ES EVTC EVDY EVGN EVH EXAM EXAR XCO EXC EXCU EXPR STAY EXTN EXR XOM FNB FNB^E FN FDS FICO FMSA FPI FFG FCB AGM AGM.A AGM^A AGM^B AGM^C FRT FSS FII FPT FMN FDX FCH FCH^A RACE FGP FOE FCAM FCAU FBR FGL FNF FNFV FIS FMO FSCE FAC FAF FBP FCF FDC FHN FHN^A FR AG FMD FNFG^B FPO FPO^A FRC FRC^A FRC^B FRC^C FRC^D FRC^E FRC^F FRC^G FFA FMY FAV FDEU FIF FSD FPF FEI FPL FCT FGB FHY FEO FAM FE FMER^A FIT OAKS OAKS^A FVE FBC DFP PFD PFO FFC FLC FLT FLTX FTK FLO FLS FLR FLY FMC FTI FMX FL F FELP FCE.A FCE.B FOR FDI FIG FTAI FSM FBHS FET FCPT FNV FC FSB BEN FT FI FCX FMS FDP FRO FSIC FCN FF FXCM GCV GCV^B GDV GDV^A GDV^D GAB GAB^D GAB^G GAB^H GAB^J GGZ GGT GGT^B GUT GUT^A GFA GCAP GBL GNT GME GPS IT GLOG GLOG^A GLOP GMT GZT GCP GNK GNRT GNRC GAM GAM^B BGC GD GEH GEK GE GEB GGP GGP^A GIS GM GM.WS.A GM.WS.B GSI GCO GWR GEL GEN GNE GNE^A G GPC GNW GEO GPRK GPE^A GGB GTY GIMO GIL GLT GKOS GSK BRSS GNL GLP GPN GSL GSL^B GLOB GMED GNC GDDY GOL GFI GG GSBD GS GS^A GS^B GS^C GS^D GS^I GS^J GS^K GS^N GSJ TFG GER GMZ GOV GPX GGG GHM GHC GPT GPT^A GRAM GVA GRP.U GPK GTN GTN.A AJX GXP GXP^A GXP^D GXP^E GWB GB GDOT GBX GHL GEF GEF.B GFF GPI GRUB PAC ASR AVAL BSMX TV GTT GSH GES GBAB GGM GPM GGE GEQ GOF GWRE GUA GLF HRB FUL HAE HK HAL HYH HBI HASI HOG HAR HMY HRS HSC HHS HGH HIG HIG.WS HNR HTS HTS^A HVT HVT.A HE HE^U HCA HCI HCJ HCP HDB HW HR HTA HLS HLS.WS HPY HL HL^B HEI HEI.A HLX HP HLF HTGC HTGX HTGY HTGZ HRTG HT HT^B HT^C HSY HTZ HES HES^A HPE HXL HF HGG HCLP ONE HIW HIL HI HRC HTH HLT HNI HMLP HEP HFC HD HMC HON HMN HZN HTF HRL HOS HPT HPT^D HST HLI HSFC^B HOV HHC HPQ HRG HSBC HSBC^A HSEA HSEB HUSI^F HUSI^G HUSI^H HNP HUBB HUBS HBM HBM.WS HPP HGT HUM HII HUN H HY IAG IBN IDA IEX IDT IHS ITW IMN IMAX IMPV IMPR IMS ICD IHC IFN IBA BLOX INFY HIFR IND ING INZ ISF ISG ISP IR IM INGR IPHI NSP IBP INST I I^A ICE IHG IFF IBM IGT IP IOC IPG IPL^D INXN IL SNOW IPI XON IVC INVN VBF VCV VTA VLT IVR IVR^B IVR^A OIA VMO VKQ VPV IVZ IQI VVR VTN VGM IIM ITG IRET IRET^ IRET^B NVTA IO IRM IRS ICL STAR STAR^D STAR^E STAR^F STAR^G STAR^I ITCB ITUB ITC ITT ESI IVH JPM JPM.WS JPM^A JPM^B JPM^D JPM^E JPM^F JPM^G JPM^H JAX JCP JGW SJM JBL JEC JHX JNS JOF JAH JCAP JKS JMP JMPB JMPC JBT BTO HEQ JHS JHI HPF HPI HPS PDT HTD HTY JW.A JW.B JNJ JCI JONE JLL JOY JPEP JFC JMEI JNPR JP JE LRN KAI KAMN KSU KSU^ KS KAR KATE KED KYE KMF KYN KYN^F KYN^G KB KBH KBR KAP KCG K KEM KMPA KMPR KMT KW KWN KEN KEG KEY KEY^G KEYS KRC KRC^G KRC^H KMB KIM KIM^I KIM^J KIM^K KMI KMI.WS KMI^A KND KFS KGC KEX KRG KKR KKR^A KFH KFI KFN^ KIO KMG KNX KNL KNOP KN KSS PHG KOP KEP KEF KF KFY KOS KRA KKD KR KRO KT KYO LB SCX LLL LQ LH LG LADR LDR LCI LPI LVS LHO LHO^H LHO^I LFL LDF LGI LAZ LOR LZB LEA LEE BWG LM LMHA LEG CVB JBK KCC KTH KTN KTP XKE LDOS LEJU LC LEN LEN.B LII LUK LVLT LXP LXP^C LXK LPL USA ASG LPT LOCK LITB LNC LNC.WS LNN LNKD LGF LAD LYV LYG SCD RIT LMT L LPX LOW LXU LTC LUB LL LXFR LXFT LUX LDL WLH LYB MTB MTB.WS MTB^ MTB^C MDC MHO MHO^A MAC CLI MGU MIC MFD BMA M MCN MSP MMP MGA MX MH^A MH^C MHNA MHNB MHNC MAIN MSCA MMD MNK MZF HYF MANU MTW MFS MN MAN MFC MRO MPC MMI MCS MRIN MHG MPX HZO MKL VAC MMC MLM MAS DOOR MTZ MA MTDR MTRN MATX MLP MMS MXL MXPT MBI MNI MKC MKC.V MDR MCD MUX MHFI MCK MDU MJN MTL MTL^ MEG MPW MED MCC MCQ MCV MCX MDLY MD MDT MRK MCY MDP MTH MTOR MER^K MER^M MER^P PIY MTR MSB MPG MEI MET MET^A MTD MXE MXF MFA MFA^B MFO MFCB MCR MGF MIN MMT MFM MFV MTG MGM KORS MAA MEP MSL MCRN MLR HIE MTX MP^D MG MTU MIXT MFG MBT MBLY MODN MOD MC MHK MOH TAP TAP.A MNR MNR^A MNR^B MORE MON MWW MCO MOG.A MOG.B MS MS^A MS^E MS^F MS^G MS^I MSK MWG MWO MWR APF CAF MSD EDD MSF IIF MOS MSI MOV MPLX MRC ICB HJV MSA MSM MSCI MSG MSGN MLI MWA MPSX MUR MUSA MVO MVC MVCB MYE NBR NC NTP NBHC NFG NGG NHI NOV NPK NNN NNN^D NNN^E SID NSA NSM NW^C NGS NGVC NRP NTZ NLS NCI NVGS NNA NM NM^G NM^H NAP NMM NAV NAV^D NCS NCR NP NEFF NNI NPTN N NSR NVRO HYB GF NWHM IRL NEWM NMFC EDU NEWR NRZ SNR NWY NYCB NYCB^U NYRT NYT NCT NCT^B NCT^C NCT^D NWL NFX NJR NEU NEM NR NHF NXRT NEP NEE NEE^C NEE^G NEE^H NEE^I NEE^J NEE^P NEE^Q NGL NMK^B NMK^C NJ NLSN NKE NMBL NTT NKA NI NL NOAH NE NBL NOK NOMD NMR OSB NORD NAO NAT JWN NSC NTL NOA NADL NRT NTI NOC NSAM NRE NRF NRF^A NRF^B NRF^C NRF^D NRF^E NWN NWE NVS NVO DNOW NQ NRG NYLD NYLD.A DCM NUS NUE NS NSH NSS JMLP NEA NUV NUW NAZ NBB NBD NKX NAC NCA NTC JCE JQC JDD NAD NVG DIAX JMF NZF NEV JPW JFR JRO NKG JGV JGH JHA JHY NXC NXN NID NQM NMY NMT NUM NMS JLS JMM NHA NMI NMO NXJ NRK NAN NNY NNC NUO NQP NPP JPI JPC NPF NPM NPI JTP JPS JHP JRI BXMX SPXX NIM NQS NXP NXQ NXR NSL JSD JTD JTA NTX NPV NIQ JMT NVR OAK OAS OXY OII OZM OCIP OCN OFG OFG^A OFG^B OFG^D OGE OIBR OIBR.C OIS ODC ORI OLN OMAM OHI OME OMC OMN ASGN ONDK OGS OLP OB OMF OKS OKE OOMA OPK OPWR OPY ORCL ORAN OA ORC OEC ORN IX ORA OSK OUT OMI OC OI OXM PAI ROYT PACD PCG PKG PANW PAM P PHX PAR PGRE PKE PKD PH PKY PE PRE^D PRE^E PRE^F PRTY PN PAYC PBF PBFX BTU PSO PEB PEB^B PEB^C PBA PGH PWE PNTA PEI PEI^A PEI^B PFSI PMT PAG PNR PEN PEP PFGC PSG PKI PBT PRGO PZE PTR PBR PBR.A PQ PFE PMC PHH PM PHI PSX PSXP PFX PNX FENG DOC PNY PDM PIR PCQ PCK PZC PCM PTY PCN PCI PDI PGP PHK PKO PFL PFN PMF PML PMX PNF PNI PYN RCS PF PNW PES PHD PHT MAV MHI PXD PJC PBI PBI^B PJT PAA PAGP PLNT PLT PAH PGEM PNC PNC.WS PNC^P PNC^Q PNM PII POL POR PKX POST PPS PPS^A POT POWR PPG PPX PPL PYS PYT PX PDS APTS PJS PGND PBH PVG PRI PPP PFG PGZ PVTD PRA PG PGR BIN PLD PRO PBB PB PL^C PL^E PRLB PSTG PFS PFK PJH PRH PRU GHY PUK PUK^ PUK^A ISD PSB PSB^S PSB^T PSB^U PSB^V TLK PEG PSA PSA^A PSA^B PSA^Q.CL PSA^R PSA^S PSA^T PSA^U PSA^V PSA^W PSA^X PSA^Y PSA^Z PHM PBYI PCF PMM PIM PMO PPT PVH PZN QTWO QEP QIHU QTS QUAD KWR NX PWR QTM DGX STR Q QUOT CTAA CTQ CTU CTV CTW CTX CTY CTZ RAX RDN RAS RAS^A RAS^B RAS^C RFT RFTA RL RPT RPT^D RRC RJD RJF RYAM RYN RTN RMAX RLGY O O^F RHT RLH RWT RBC RGC REG REG^F REG^G RM RF RF^A RF^B RGS RGA RZA RS RENX RELX RNR RNR^C RNR^E SOL RENN RSG RMD REN RFP RSO RSO^A RSO^B RSO^C QSR RH RPAI RPAI^A REV REX REXR RXN RAI RICE RMP RNG RIO RBA RAD RIV RLI RLJ RRTS RHI ROK COL RCI ROG ROL ROP RRMS RST RSE RDC RY RY^S RY^T RBS RBS^E RBS^F RBS^G RBS^H RBS^I RBS^L RBS^R RBS^S RBS^T RCL RDS.A RDS.B RGT RMT RVT RES RPM RSPP RT RKUS RTEC R RYI RHP SBR SB SB^B SB^C SB^D SFE CRM SMM SBH SJT SN SDT SDR PER SNY SC SOV^C SAP SAQ SAR SSL BFS BFS^C SCG SLB SWM SAIC SALT SLTB SBNA SBNB STNG SMG LBF KHI KMM KTF KST KSM SA CKH SDRL SDLP SEE SSW SSW^C SSW^D SSW^E SSWN SEAS JBN JBR SIR SEM SGZA SEMG SMI SRE SNH SNHN SNHO ST SXT SQNS SRG SCI SERV NOW SSE SHAK SJR SHLX SHW SHG SFL SHOP SSTK SBGL SIG SBY SSNI SLW SPG SPG^J SSD SHI SIX SJW SKM SKX SLG SLG^I SM SFS SNN AOS SNA SQM SLRA SAH SON SNE BID SFUN SOR SJI SXE SCE^F SCE^G SCE^H SCE^J SCE^K SO SOJA SCCO LUV SWX SWN SWNC SSS SPA SPE SE SEP SPB TRK SPR SRC SRLP S SPXC FLOW SQ JOE STJ STAG STAG^A STAG^B STAG^C SSI SMP SXI SWH SWJ SWK STN SGU SRT HOT HOT$ STWD STT STT^C STT^D STT^E STO SPLP SCS SCM SCQ SCL STE STL STC SF SFN SWC STM SGY EDF EDI SGM STON SRI STOR SGL GJH GJO GJS SYK RGR SPH SCNB SMFG INN INN^A INN^B INN^C SUM SMLP SUI SUI^A SLF SXCP SXC SU SUNE SXL SUN SHO SHO^E STI STI.WS.A STI.WS.B STI^A STI^E SPN SUP SVU SWFT SWZ SYF SYT SNX SNV SNV^C GJP GJR GJT GJV SYY SYX DATA TAHO TLRD TWN TSM XRS TAL TLN TEGP TEP SKT TAOM NGLS^A TRGP TGT TARO TTM TCO TCO^J TCO^K TMHC TCP TCB TCB.WS TCB^B TCB^C TCPI TSI TEL TMH TISI TCK TE TK TGP TOO TOO^A TOO^B TNK GCI TGNA TRC HQH THQ HQL THW TDOC TEO TI TI.A TDY TFX VIV TEF TDA TDE TDI TDJ TDS TU TDF EMF TEI GIM TPX TS THC TNC TEN TVC TVE TDC TER TEX TX TNH TRNO TRNO^A TSO TLLP TTI TEVA TPL TGH TXT TXTR TTF AES AES^C BX SCHW SCHW^B SCHW^C SCHW^D SRV GRX GRX^A GRX^B GDL GDL^B THG THGA RUBI TRV TMO THR TPRE TSLF TCRX TCRZ TRI THO TDW TIER TIF TLYS TSU TIME TWC TWX TKR TMST TWI TJX TOL TR BLD TMK TMK^B TMK^C TTC TD NDP TYG NTG TTP TPZ TSS TOT TOWR TSQ TM TSLX TAC TRP TCI TDG TLP RIG RIGP TGS TRU TA TANN TANO TANP TVPT TRR TREC TG THS TRMR TREX TY TY^ TPH TCAP TCCA TCCB TRCO TPUB TSL TNET TRN TSE TPVG TPVZ GTS TGI TROX TBI TRUP TNP TNP^B TNP^C TNP^D TUMI TUP TKC TKF TRQ TPC TWTR TWO TYC TYL TSN TSNU USB USB^A USB^H USB^M USB^N USB^O USPH SLCA UBS UBS^D UCP UGI UPL UGP UMH UMH^A UMH^B UA UA.C UFI UNF UN UL UNP UIS UNT UAL UDR UMC UPS URI USM UZA UZB UZC X UTX UNH UTL UNVR UAM UVV UHT UHS UVE UTI UNM UE UBA UBP UBP^F UBP^G USAC USNA USDP USG BIF VFC EGY MTN VALE VALE.P VRX VLO VLP VHI VR VLY VLY.WS VLY^A VMI VAL VNTV VAR VGR VVC VEC VEDL VEEV VTRB VTR VER VER^F PAY VRTV VZ VZA VET VVI VCO VNCE VMEM VIPS VGI DCA V VSH VPG VSTO VC VSI VSLR VMW VOC VCRA VG VNO VNO^G VNO^I VNO^J VNO^K VNO^L VJET IAE IHD VOYA IGA IGD IDE IID IRR PPR VTTI VMC WTI WPC WRB WRB^B WRB^C GRA GWW WNC WBC WDR WAGE WD WMT DIS WAC WRE WCN WM WAT WSO WSO.B WTS W WCIC WFT WBS WBS^E WEC WTW WRI WMK WCG WFC WFC.WS WFC^J WFC^L WFC^N WFC^O WFC^P WFC^Q WFC^R WFC^T WFC^V WFC^W WFE^A EOD HCN HCN^I HCN^J WAIR WCC WST WR WAL WEA TLI ESD EMD GDO EHI GDF HIX HIO HYI IGI MHY MMU WMC DMO MTT MHF MNP GFY SBW WIW WIA WGP WES WNRL WNR WU WAB WLK WLKP WMLP WBK WRK WHG WEX WY WY^A WGL WHR WTM WSR WWAV WLL WG WMB WPZ WSM WGO FUR WIT WNS WWW WF WDAY WK INT WPT WWE WOR WPG WPG^H WPG^I WPX WPXP WYN XTLY XEL XHR XRM XRX XIN XL XOXO XPO XUE XYL YDKN AUY YZC YELP YGE YRD YPF YUM YUME ZFC ZAYO ZEN ZPIN ZBH ZB^A ZB^F ZB^G ZB^H ZBK ZOES ZTS ZF ZTR".split()
NASDAQ_STOCKS = "TFSC TFSCR TFSCU TFSCW PIH FLWS FCTY FCCY SRCE VNET TWOU JOBS CAFD EGHT AVHI SHLM AAON ABAX ABY ABGB ABEO ABEOW ABIL ABMD AXAS ACTG ACHC ACAD ACST AXDX XLRN ANCX ARAY VXDN VXUP ACRX ACET AKAO ACHN ACIW ACRS ACNB ACOR ACTS ACPW ATVI ACTA ACUR ACXM ADMS ADMP ADAP ADUS AEY IOTS ADMA ADBE ADTN ADRO AAAP AEIS AITP AMD ADXS ADXSW MAUI YPRO AEGR AEGN AGLE AEHR AMTX AEPI AERI AVAV AEZS AEMD AFMD AGEN AGRX AGYS AGIO AGFS AGFSW AIMT AIRM AIRT ATSG AMCN AIXG AKAM AKTX AKBA AKER AKRX ALRM ALSK AMRI ABDC ADHD ALDR ALDX ALXN ALXA ALCO ALGN ALIM ALKS ABTX ALGT AFOP AIQ AHGP ARLP AHPI AMOT ALQA ALLT MDRX AFAM ALNY AOSL GOOG GOOGL SMCP ATEC ASPS AIMC AMAG AMRN AMRK AYA AMZN AMBC AMBCW AMBA AMCX DOX AMDA AMED UHAL ATAX AMOV AAL AGNC AGNCB AGNCP MTGE MTGEP ACSF ACAS GNOW AETI AMIC AMNB ANAT APEI ARII AMRB ASEI AMSWA AMSC AMWD CRMT ABCB AMSF ASRV ASRVP ATLO AMGN FOLD AMKR AMPH AMSG AMSGP ASYS AFSI AMRS ANAC ADI ALOG AVXL ANCB ABCW ANDA ANDAR ANDAU ANDAW ANGI ANGO ANIP ANIK ANSS ATRS ANTH ABAC ZLIG ATNY APIC APOG APOL AINV AMEH APPF AAPL ARCI APDN APDNW AGTC AMAT AMCC AAOI AREX APRI APTO AQMS AQXP AUMA AUMAU AUMAW ARDM ARLZ PETX ABUS ARCW ABIO RKDA ARCB ACGL APLP ACAT ARDX ARNA ARCC AGII AGIIL ARGS ARIS ARIA ARKR ARMH ARTX ARWA ARWAR ARWAU ARWAW ARQL ARRY ARRS DWAT AROW ARWR ARTNA ARTW PUMP ASBB ASNA ASND ASCMA APWC ASML AZPN ASMB ASFI ASTE ALOT ATRO ASTC ASUR ATAI ATRA ATHN ATHX AAPC AAME ACBI ACFC ATNI ATLC AAWW AFH TEAM ATOS ATRC ATRI ATTU LIFE AUBN AUDC AUPH EARS ABTL ADSK AGMX ADP AAVL AVNU AVEO AVXS AVNW AVID AVGR CAR AWRE ACLS AXGN AXSM AXTI BCOM RILY BOSC BEAV BIDU BCPC BWINA BWINB BLDP BANF BANFP BKMU BOCH BMRC BKSC BOTJ OZRK BFIN BWFG BANR BZUN BHAC BHACR BHACU BHACW BBSI BSET BYBK BYLK BV BBCN BCBP BECN BSF BBGI BEBE BBBY BGNE BELFA BELFB BLPH BLCM BNCL BNFT BNTC BNTCW BGCP BGFV BIND ORPN BASI BCDA BIOC BCRX BIOD BDSI BIIB BIOL BLFS BOLT BLRX BMRN BVXV BVXVW BPTH BIOS BBC BBP BSTC BSTG BSPM TECH BEAT BITI BDMS BJRI BBOX BDE BLKB BBRY HAWK BKCC ADRA ADRD ADRE ADRU BLMN BCOR BLBD BUFF BHBK NILE BLUE BKEP BKEPP BPMC ITEQ STCK BNCN BOBE BOFI BOFIL WIFI BOJA BOKF BNSO BPFH BPFHP BPFHW EPAY BLVD BLVDU BLVDW BOXL BCLI BBRG BBEP BBEPP BDGE BLIN BRID BCOV AVGO BSFT BVSN BYFC BWEN BRCD BRKL BRKS BRKR BMTC BLMT BSQR BWLD BLDR BUR CFFI CHRW CA CCMP CDNS CDZI CACQ CZR CSTE PRSS CLBS CLMS CHY CHI CCD CFGE CHW CGO CSQ CAMP CVGW CFNB CALA CALD CALM CLMT ABCD CAC CAMT CSIQ CGIX CPHC CBNJ CPLA CBF CCBG CPLP CSWC CPTA CLAC CLACU CLACW CFFN CAPN CAPNW CAPR CPST CARA CARB CBYL CRDC CFNL CRME CSII CATM CDNA CECO CTRE CKEC CLBH CARO CART CRZO TAST CRTN CARV CASM CACB CSCD CWST CASY CASI CASS CATB CBIO CPRX CATY CATYW CVCO CAVM CBFV CNLM CNLMR CNLMU CNLMW CBOE CDK CDW CECE CPXX CELG CELGZ CLDX CLRB CLRBW CLLS CBMG CLSN CYAD CEMP CETX CSFL CETV CFBK CENT CENTA CVCY CFCB CENX CNBKA CNTY CPHD CRNT CERC CERCW CERCZ CERE CERN CERU CERS KOOL CEVA CSBR CYOU HOTR HOTRW CTHR GTLS CHTR CHFN CHKP CHEK CHEKW CEMI CHFC CCXI CHMG CHKE CHEV CHMA CBNK PLCE CMRX CADC CALI CAAS CBAK CBPO CCCL CCCR CCRC JRJC HGSH CNIT CJJD HTHT CHNR CREG CNTF CXDC CNYD CCIH CNET IMOS CHSCL CHSCM CHSCN CHSCO CHSCP CHDN CHUY CDTX CIFC CMCT CMPR CINF CIDM CTAS CPHR CRUS CSCO CTRN CZNC CZWI CZFC CIZN CTXS CHCO CIVB CIVBP CDTI CLNE CLNT CLFD CLRO CLIR CBLI CSBK CLVS CMFN CME CCNE CISG CNV CWAY COBZ COKE CDRB CDXS CVLY JVA CCOI CGNT CGNX CTSH COHR CHRS COHU CLCT COLL CIGI CBAN CLCD COLB COLM CMCO CBMX CBMXW CMCSA CBSH CBSHP CUBN CVGI COMM CSAL JCS ESXB CCFI CYHHZ CTBI CWBC COB CVLT CGEN CPSI CTG SCOR CHCI CMTL CNAT CNCE CXRX CCUR CDOR CDORO CDORP CFMS CONG CNFR CNMD CTWS CNOB CNXR CONN CNSL CWCO CPSS CFRX CFRXW CTRV CTRL CPRT COYN COYNW CRBP CORT BVA CORE CORI CSOD CRVL CRVS COSI CSGP COST CPAH ICBK CVTI COVS COWN COWNL PMTS CPSH CRAI CBRL BREW CRAY CACC GLDI CREE CRESY CRTO CROX CCRN XRDC CRDS CRWS CRWN CYRX CYRXW CSGS CCLP CSPI CSWI CSX CTCM CTIC CTIB CTRP CUNB CUI CPIX CMLS CRIS CUTR CVBF CVV CYAN CYBR CYBE CYCC CYCCP CBAY CYNA CYNO CY CYRN CONE CYTK CTMX CYTX CTSO CYTR DJCO DAKT DAIO DTLK DRAM DWCH PLAY DTEA DWSN DBVT DHRM DFRG TACO TACOW DCTH DGAS DELT DELTW DENN XRAY DEPO DSCI DERM DEST DXLG DSWL DTRM DXCM DHXM DHIL FANG DCIX DRNA DFBG DGII DMRC DRAD DGLY APPS DCOM DMTX DIOD DPRX DISCA DISCB DISCK DSCO DISH DVCR SAUC DLHC DNBF DLTR DGICA DGICB DMLP DORM EAGL EAGLU EAGLW DDAY DRWI DRWIW DWA DRYS DSKX DSPG CADT CADTR CADTU CADTW DTSI DLTH DNKN DRRX DXPE BOOM DYSL DYNT DVAX ETFC EBMT EGBN EGLE EGRX ELNK EWBC EACQ EACQU EACQW EML EVBS EVGBC EVSTC EVLMC EBAY EBAYL EBIX ELON ECHO ECTE SATS EEI ECAC ECACR ECACU ESES EDAP EDGE EDGW EDIT EDUC EFUT EGAN EGLT EHTH EIGR LOCO EMITF ESLT ERI ELRC ESIO EA EFII ELSE ELEC ELECU ELECW EBIO RDEN CAPX ESBK LONG ELTK EMCI EMCF EMKR EMMS NYNY ERS ENTA ECPG WIRE ENDP ECYT ELGX EIGI WATT EFOI ERII EXXI ENOC ENG ENPH ESGR ENFC ENTG ENTL ETRM EBTC EFSC EGT ENZN ENZY EPIQ EPRS EPZM PLUS EQIX EQFN EQBK EAC ERIC ERIE ESCA ESMC ESPR ESSA EPIX ESND ESSF ETSY CLWT EEFT ESEA EVEP EVK EVLV EVOK EVOL EXA EXAS EXAC EXEL EXFO EXLS EXPE EXPD EXPO ESRX EXTR EYEG EYEGW EZPW FFIV FB FCS FRP FWM FALC DAVE FARM FFKT FMNB FARO FAST FATE FBSS FBRC FDML FNHC FEIC FHCO FENX GSM FCSC FGEN ONEQ LION FDUS FRGI FSAM FSC FSCFL FSFR FITB FITBI FNGN FISI FNSR FNJN FNTC FNTCU FNTCW FEYE FBNC FNLC FRBA BUSE FBIZ FCAP FCFS FCNCA FCLF FCBC FCCO FCFP FBNK FDEF FFBC FFBCW FFIN THFF FFNW FFWM FGBI INBK FIBK FRME FMBH FMBI FNBC FNFG FNWB FSFG FSLR FSBK FPA BICK FBZ FCAN FTCS FCA FDT FDTS FVC FV IFV FEM FEMB FEMS FTSM FEP FEUZ FGM FTGC FTHI HYLS FHK FTAG FTRI FPXI YDIV SKYY FJP FEX FTC FTA FLN FTLB LMBS FMB FMK FNX FNY FNK FAD FAB MDIV QABA QCLN GRID CIBR CARZ RDVY FONE TDIV QQEW QQXT QTEC AIRR QINC FTSL FYX FYC FYT FKO FCVT FDIV FSZ FTW TUSA FKU FUNC SVVC FMER FSV FISV FIVE FPRX FIVN FLML FLKS FLXN SKOR LKOR MBSD ASET QLC FLXS FLEX FLIR FLDM FFIC FOMX FOGO FONR FES FORM FORTY FORR FTNT FBIO FWRD FORD FWP FOSL FMI FXCB FOXF FRAN FELE FRED FREE RAIL FEIM FRPT FTR FTRPR FRPH FSBW FTD FSYS FTEK FCEL FORK FULL FULLL FLL FULT FSNN FFHL GK WILC GAIA GLPG GALT GALTU GALTW GALE GLMD GLPI GPIC GRMN GGAC GGACR GGACU GGACW GARS GCTS GENC GNCMA GFN GFNCP GFNSL GENE GNMK GNCA GHDX GNST GNTX THRM GNVC GTWN GEOS GABC GERN GEVO ROCK GIGM GIGA GIII GILT GILD GBCI GLAD GLADO GOOD GOODN GOODO GOODP GAIN GAINN GAINO GAINP LAND GLBZ GBT ENT GBLI GBLIZ GPAC GPACU GPACW SELF GSOL ACTX QQQC SOCL ALTY SRET YLCO GBIM GLBS GLRI GLUU GLYC GOGO GLNG GMLP GLDC GDEN GOGL GBDC GTIM GPRO GMAN GRSH GRSHU GRSHW GPIA GPIAU GPIAW LOPE GRVY GBSN GLDD GSBC GNBC GRBK GPP GPRE GCBC GLRE GRIF GRFS GRPN OMAB GGAL GSIG GSIT GSVC GTXI GBNK GFED GUID GIFI GURE GPOR GWPH GWGH GYRO HEES HLG HNRG HALL HALO HBK HMPR HBHC HBHCL HNH HAFC HNSN HQCL HDNG HLIT HRMN HRMNU HRMNW TINY HBIO HCAP HCAPL HAS HA HCOM HWKN HWBK HAYN HDS HIIQ HCSG HQY HSTM HWAY HTLD HTLF HTWR HTBX HSII HELE HMNY HMTV HNNA HCAC HCACU HCACW HSIC HERO HTBK HFWA HEOP HCCI MLHR HRTX HSKA HFFC HIBB HPJ HIHO HIMX HIFS HSGX HMNF HMSY HOLI HOLX HBCP HOMB HFBL HMST HTBI CETC HOFT HFBC HBNC HZNP HRZN HDP HMHC HWCC HOVNP HBMD HSNI HTGM HUBG HSON HDSN HBAN HBANO HBANP HURC HURN HTCH HCM HBP HDRA HDRAR HDRAU HDRAW HYGS IDSY IAC IKGH IBKC IBKCP ICAD IEP ICFI ICLR ICON ICUI IPWR INVE IDRA IDXX DSKY IROQ IRG RXDX IIVI KANG IKNX ILMN ISNS IMMR ICCC IMDZ IMNP IMGN IMMU IPXL IMMY INCR SAAS INCY INDB IBCP IBTX IDSA INFN INFI IPCC III IFON IMKTA INWK INNL INOD IPHS IOSP ISSC INVA INGN ITEK INOV INO NSIT ISIG INSM IIIN PODD INSY NTEC IART IDTI IESC INTC IQNT IPCI IPAR IBKR ININ ICPT ICLD ICLDW IDCC TILE IMI INAP IBOC ISCA IGLD IIJI IDXG XENT INTX ISIL IILG IILGV IVAC INTL INTLL ITCI IIN INTU ISRG INVT SNAK ISTR ISBC ITIC NVIV IVTY IONS IPAS IPGP IRMD IRIX IRDM IRDMB IRBT IRWD IRCP SLQD TLT AIA COMT IXUS IFEU IFGL IGF GNMA JKI ACWX ACWI AAXJ EWZS MCHI SCZ EEMA EEML EUFN IEUS ENZL QAT UAE IBB SOXX EMIF ICLN WOOD INDY ISHG IGOV ISLE ISRL ITI ITRI ITRN ITUS XXIA IXYS IZEA JJSF MAYS JBHT JCOM JASO JKHY JACK JXSB JAGX JAKK JMBA JRVR JSML JSMD JASN JASNW JAZZ JD JSYNU JBLU JTPY JCTCF DATE JST JIVE WYIG WYIGU WYIGW JBSS JOUT JNP JUNO KTWO KALU KMDA KNDI KPTI KBSF KCAP KRNY KELYA KELYB KMPH KFFB KERX KEQU KTEC KTCC KFRC KE KBAL KIN KGJI KINS KONE KIRK KITE KTOV KTOVW KLAC KLRE KLREU KLREW KLXI KONA KZ KOPN KRNT KOSS KWEB KTOS KUTV KLIC KURA KVHI FSTR LJPC DRIO DRIOW LSBK LSBG LBAI LKFN LAKE LRCX LAMR LANC LNDC LARK LMRK LE LSTR LNTH LTRX LPSB LSCC LAWS LAYN LCNB LDRH LBIX LGCY LGCYO LGCYP LTXB DDBI EDBI LVHD UDBI LMAT TREE LXRX LGIH LHCG LBRDA LBRDK LBTYA LBTYB LBTYK LILA LILAK LVNTA LVNTB QVCA QVCB LMCA LMCB LMCK TAX LTRPA LTRPB LPNT LCUT LFVN LWAY LGND LTBR LPTH LLEX LIME LLNW LMNR LINC LECO LIND LINDW LLTC LNCO LINE LBIO LIOX LPCN LQDT LFUS LIVN LOB LIVE LPSN LKQ LMFA LMFAW LMIA LOGI LOGM EVAR CNCR LORL LOXO LPTN LPLA LRAD LYTS LULU LITE LMNX LMOS LUNA MBTF MTSI MCBC MFNC MCUR MGNX MAGS MGLN MPET MGIC CALL MNGA MGYR MHLD MHLDO MSFG COOL MMYT MBUU MLVF MAMS MANH LOAN MNTX MTEX MNKD MANT MAPI MARA MCHX MARPS MRNS BBH GNRX PPH MKTX MKTO MRKT MRLN MAR MBII MRTN MMLP MRVL MASI MTCH MTLS MTRX MAT MATR MATW MFRM MTSN MXIM MXWL MZOR MBFI MBFIP MCFT MGRC MDCA MCOX TAXI MTBC MTBCP MNOV MDSO MDGS MDVN MDWD MDVX MDVXW MEET MEIP MPEL MLNX MELR MEMP MRD MENT MTSL MELI MBWM MERC MBVT MRCY EBSB VIVO MMSI MACK MSLI MLAB MESO CASH MBLX MEOH MFRI MGCD MGEE MGPI MCHP MU MICT MICTW MSCC MSFT MSTR MVIS MPB MTP MCEP MBRG MBCN MSEX MOFG MIME MDXG MNDO MB NERV MRTX MIRN MSON MIND MITK MITL MKSI MMAC MINI MOBL MOCO MDSY MLNK MOKO MOLG MNTA MOMO MCRI MNRK MDLZ MGI MPWR TYPE MNRO MRCC MNST MHGC MORN MOSY MPAA MDM MRVC MSBF MSG MTSC LABL MFLX MFSF MYL MYOK MYOS MYRG MYGN NBRV NAKD NNDM NANO NSPH NSTG NK NSSC NDAQ NTRA NATH NAUH NKSH FIZZ NCMI NCOM NGHC NGHCO NGHCP NGHCZ NHLD NATI NATL NRCIA NRCIB NSEC NWLI NAII NHTC NATR BABY NAVI NBCP NBTB NCIT NKTR NEOG NEO NEON NEOS NEOT NVCN NRX NEPT UEPS NETE NTAP NTES NFLX NTGR NLST NTCT NTWK CUR NBIX NDRM NURO NUROW NSIG NYMT NYMTO NYMTP NLNK NEWP NWS NWSA NEWS NEWT NEWTZ NXST NVET NFEC EGOV NICE NICK NCBS NIHD NVLS NMIH NNBR NDLS NORT NDSN NSYS NTK NBN NTIC NTRS NTRSP NFBK NRIM NWBI NWBO NWBOW NWPX NCLH NWFL NVFY NVMI NVDQ MIFI NVAX NVCR NVGN NTLS NUAN NMRX NUTR NTRI NUVA NVTR QQQX NVEE NVEC NVDA NXPI NXTM NXTD NXTDW NYMX OIIM OVLY OASM OBCI OPTT ORIG OSHC OCFC OCRX OCLR OFED OCUL OCLS OCLSW OMEX ODP OFS OHAI OVBC OHRP ODFL OLBK ONB OPOF OSBC OSBCP OLLI ZEUS OFLX OMER OMCL ON OTIV OGXI OMED ONTX ONCS ONTY OHGI ONVI OTEX OPXA OPXAW OPGN OPGNW OPHT OBAS OCC OPHC OPB ORMP OSUR ORBC ORBK ORLY OREX SEED OESX ORIT ORRF OFIX OSIS OSIR OSN OTEL OTG OTIC OTTR OUTR OVAS OSTK OXBR OXBRW OXFD OXLC OXLCN OXLCO OXGN PFIN PTSI PCAR PACE PACEU PACEW PACB PCBK PEIX PMBC PPBI PAAC PAACR PAACU PAACW PSUN PCRX PACW PTIE PAAS PNRA PANL PZZA FRSH PRGN PRGNL PRTK PRXL PCYG PSTB PKBK PRKR PKOH PARN PTNR PBHC PATK PNBK PATI PEGI PDCO PTEN PAYX PCTY PYDS PYPL PBBI PCCC PCMI PCTI PDCE PDFS PDLI PDVW SKIS PGC PEGA PCO PENN PFLT PNNT PWOD PTXP PEBO PEBK PFBX PFIS PBCT PUB PRCP PPHM PPHMP PRFT PFMT PERF PERI PESI PTX PERY PGLC PETS PFSW PGTI PHII PHIIK PAHC PHMD PLAB PICO PIRS PPC PME PNK PNFP PPSI PXLW PLPM PLXS PLUG PLBC PSTI PLXP PMV PBSK PNTR PCOM PLCM POOL POPE PLKI BPOP BPOPM BPOPN PBIB PTLA PBPB PCH POWL POWI PSIX PDBC DWIN DWTR IDLB PRFZ PAGG PSAU IPKW LDRI LALT PNQI QQQ USLB PSCD PSCC PSCE PSCF PSCH PSCI PSCT PSCM PSCU PRAA PRAH PRAN PFBC PLPC PFBI PINC LENS PRGX PSMT PBMD PNRG PRMW PRIM PSET PY PRZM PVTB PVTBP PDEX IPDN PFIE PGNX PRGS DNAI PFPT PRPH PRQR BIB UBIO TQQQ ZBIO SQQQ BIS PSEC PRTO PTI PRTA PWX PVBC PROV PBIP PSDV PMD PTC PTCT PULB PULM PCYO PXS QADA QADB QCRH QGEN QIWI QKLS QLIK QLGC QLTI QRVO QCOM QSII QBAK QLYS QRHC QUIK QDEL QPAC QPACU QPACW QNST QUMU QUNR QTNT RRD RADA RDCM ROIA ROIAK RSYS RDUS RDNT RDWR RMBS RAND RLOG GOLD RPD RPTP RAVE RAVN ROLL RICK RCMT RLOC RDI RDIB RGSE RELY RNWK RP UTES DAX QYLD RCON REPH RRGB RDHL REDF REGN RGNX DFVL DFVS DGLD DLBL DLBS DSLV DTUL DTUS DTYL DTYS FLAT SLVO STPP TAPR TVIX TVIZ UGLD USLV VIIX VIIZ XIV ZIV RGLS REIS RELV RLYP MARK RNST REGI RNVA RNVAW RCII RTK RGEN RPRX RBCAA FRBK RSAS REFR RESN REXI RECN ROIC SALE RTRX RVNC RBIO RVLT RWLK REXX RFIL RGCO RIBT RIBTW RELL RIGL NAME RNET RITT RITTW RTTR RMI RVSB RLJE RMGN ROBO FUEL RMTI RCKY RMCF RSTI ROKA ROSG ROST ROVI RBPAA RGLD RPXC RRM RTIX RBCN RUSHA RUSHB RUTH RXII RYAAY STBA SANW SBRA SBRAP SABR SAEX SAFT SAGE SGNT SAIA SAJA SALM SAL SAFM SNDK SASR SGMO SANM GCVRZ SPNS SRPT SBFG SBFGP SBAC SCSC SMIT SCHN SCHL SCLN SGMS SQI SNI SCYX SEAC SBCF STX SHIP SRSC SHLD SHLDW SHOS SPNE SGEN EYES SNFCA SEIC SLCT SCSS SIGI LEDS SMLR SMTC SENEA SENEB SNMX SRTS SQNM SQBG MCRB SREV SFBS SEV SVBI SGOC SMED SHSP SHEN SHLO SCCI SHPG SCVL SHBI SHOR SFLY SIFI SIEB SIEN BSRR SWIR SIFY SIGM SGMA SGNL SBNY SBNYW SLGN SILC SGI SLAB SIMO SPIL SRAQU SSRI SAMG SFNC SLP SINA SBGI SINO SVA SIRI SRVA SITO SZMK SKUL SKYS SKLN MOBI SPU SKYW SWKS ISM JSM OSM SLM SLMAP SLMBP SMT SMBK SWHC SMSI SMTX LNCE SODA SOHU SLRC SUNS SCTY SEDG SZYM SONC SOFO SONS SPHS SORL SRNE SOHO SOHOL SOHOM SFBC SSB SOCB SFST SMBC SONA SBSI OKSB SP SPAN SBSA SGRP SPKE ONCE SPAR SPTN SPPI ANY SPEX SPI SAVE SPLK SPOK SPWH SBPH FUND SFM SPSC SSNC STAA STAF STMP STLY SPLS SBLK SBLKL SBUX STRZA STRZB STFC STBZ SNC STDY GASS STLD SMRT SBOT STEM STML STXS SRCL SRCLP STRL SHOO SSFN SYBT BANX SGBK SSKN SSYS STRT STRS STRA STRM SBBP STB SCMP SUMR SMMF SSBI SMMT SNBC SNHY SNDE SEMI SNSS STKL SPWR RUN SBCP SSH SUNW SMCI SPCB SCON SGC SUPN SPRT SGRY SCAI SRDX SBBX SIVB SIVBO SYKE SYMC SSRG SYNC SYNL SYNA SNCR SNDX SGYP SGYPU SGYPW ELOS SNPS SNTA SYNT SYMX SYUT SYPR SYRX TROW TTOO TAIT TTWO TLMR TNDM TLF TNGO TANH TEDU TASR TATT TAYD TCPC AMTD TEAR TECD TCCO TTGT TGLS TGEN TNAV TTEC TLGT TENX GLBL TERP TRTL TRTLU TRTLW TBNK TSRO TESO TSLA TESS TSRA TTEK TLOG TTPH TCBI TCBIL TCBIP TCBIW TXN TXRH TFSL TGTX ABCO ANDE TBBK BONT CG CAKE CHEF TCFC DSGX DXYN ENSG XONE FINL FBMS FLIC TFM GT HABT HCKT HAIN CUBA INTG JYNT KEYW KHC MDCO MIK MIDD NAVG STKS PCLN PRSC BITE RMR SPNC ULTI YORW NCTY TBPH TST TCRD THLD TICC TTS TIL TSBK TIPT TITN TTNP TIVO TMUS TMUSP TBRA TKAI TNXP TISA TOPS TORM TRCH TSEM TWER CLUB TOWN TCON TSCO TWMC TACT TRNS TBIO TGA TTHI TZOO TRVN TCBK TRIL TRS TRMB TRIB TRIP TSC TBK TROV TROVU TROVW TRUE THST TRST TRMK TSRI TTMI TUBE TCX TUES TOUR HEAR TUTI TUTT FOX FOXA TWIN TRCB USCR PRTS USEG GROW UREE UBIC UBNT UFPT ULTA UCTT RARE ULBI ULTR UTEK UMBF UMPQ UNAM UNIS UBSH UNB UNXL QURE UBCP UBOH UBSI UCBA UCBI UCFC UDF UBNK UFCS UIHC UNFI UNTD UBFO USBI USLM UTHR UG UNTY OLED UEIC UFPI USAP UACL UVSP UPIP UPLD URRE URBN ECOL USAT USATP USAK USMD UTMD UTSI VALX VALU VNDA VWOB VNQI VGIT VCIT VIGI VYMI VCLT VGLT VMBS VNR VNRAP VNRBP VNRCP VONE VONG VONV VTWO VTWG VTWV VTHR VCSH VGSH VTIP BNDX VXUS VRNS VDSI VBLT VASC VBIV WOOF VECO APPY VRA VCYT VSTM VCEL VRNT VRSN VRSK VBTX VRML VSAR VTNR VRTX VRTB VIA VIAB VSAT VIAV VICL VICR CIZ CEZ CID CIL CFO CFA CSF CDC CDL CSB CSA VBND VUSE VIDI VDTH VRAY VKTX VKTXW VBFC VLGEA VIP VNOM VIRC VA VIRT VSCP VRTS VRTU VISN VTAE VTL VVUS VOD VLTC VOXX VYGR VRNG VSEC VTVT VUZI VWR WGBS WBA WRES WAFD WAFDW WASH WFBI WSBF WVE WNFM WAYN WSTG WDFC FLAG WEB WBMD WB WEBK WEN WERN WSBC WTBA WSTC WMAR WABC WBB WSTL WDC WFD WLB WPRT WEYS WHLR WHLRP WHLRW WHF WHFBL WFM WILN WHLM WVVI WVVIP WLDN WLFC WLTW WIBC WIN WING WINA WINS WTFC WTFCM WTFCW AGND AGZD HYND HYZD CXSE EMCG EMCB DGRE DXGE WETF DXJS JGBB DXKW GULF CRDT DGRW DGRS DXPS UBND WIX WLRH WLRHU WLRHW WMIH WBKC WWD WKHS WRLD WOWO WPCS WPPGY WMGI WMGIZ WSFS WSFSL WSCI WVFC WYNN XBIT XELB XCRA XNCR XBKS XENE XNPT XGTI XGTIW XLNX XOMA XPLR XCOM XTLB XNET MESG YHOO YNDX YOD YCB YRCW YECO YY ZFGN ZAGG ZAIS ZBRA ZLTQ ZHNE Z ZG ZN ZNWAA ZION ZIONW ZIONZ ZIOP ZIXI ZGNX ZSAN ZUMZ ZYNE ZNGA".split()


def main():
    print "Downloading Stock Data..."
    skip_count = 0
    url_opener = urllib.URLopener()
    for stock in (NYSE_STOCKS + NASDAQ_STOCKS):
        try:
            url_opener.retrieve("http://real-chart.finance.yahoo.com/table.csv?s=" + stock +
                                "&a=00&b=1&c=2006&d=00&e=1&f=2016&g=d&ignore=.csv",
                                "/s/salem/a/nobackup/cs435/owenrd/" + stock + ".csv")
        except IOError:
            skip_count += 1
            continue

    print "Download Completed Successfully with", skip_count, "skipped"

if __name__ == '__main__':
    main()