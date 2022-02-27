import csv

array = [['-149', '2', '397', '997', '34.90159175', '-256'], ['-148', '5', '397', '997', '45.48797607', '-105'], ['-147', '5', '395', '999', '42.39445106', '8351'], ['-146', '6', '395', '998', '62.993455', '7319'], ['-145', '7', '395', '1003', '36.52834586', '1782'], ['-144', '8', '393', '999', '46.50379914', '3498'], ['-142', '11', '393', '999', '66.0922871', '7956'], ['-137', '11', '387', '1003', '51.21155627', '7983'], ['-136', '11', '386', '1004', '30.97462127', '7050'], ['-134', '16', '379', '1003', '58.36435604', '7167'], ['-133', '17', '377', '998', '57.91002401', '308'], ['-132', '18', '376', '1000', '63.54101208', '6047'], ['-132', '20', '375', '1003', '37.61136464', '612'], ['-132', '20', '374', '995', '54.4096687', '4865'], ['-130', '21', '373', '1001', '53.52756653', '2546'], ['-129', '21', '371', '1004', '46.16028928', '5259'], ['-129', '21', '367', '1001', '42.88797716', '1740'], ['-128', '21', '364', '996', '55.3387081', '478'], ['-128', '22', '362', '1004', '53.07891981', '-373'], ['-128', '25', '361', '999', '35.10130178', '726'], ['-126', '26', '360', '997', '54.10494435', '2626'], ['-126', '26', '360', '1000', '64.29808852', '6578'], ['-124', '27', '359', '997', '61.68716406', '8430'], ['-124', '28', '359', '997', '66.15363465', '8124'], ['-123', '31', '357', '1004', '54.8690698', '400'], ['-123', '32', '356', '1001', '68.91439706', '5104'], ['-123', '36', '353', '998', '66.99143585', '7519'], ['-122', '37', '352', '1000', '33.66324873', '8268'], ['-121', '40', '350', '997', '60.4297589', '6109'], ['-120', '41', '349', '996', '34.34545314', '4322'], ['-119', '43', '347', '1004', '53.4506689', '412'], ['-119', '43', '344', '1004', '42.88971365', '5565'], ['-119', '45', '343', '999', '51.59245058', '6566'], ['-118', '47', '343', '1004', '54.87035868', '3580'], ['-115', '48', '342', '1003', '64.27912924', '8078'], ['-114', '50', '342', '1003', '37.702405', '5557'], ['-113', '50', '341', '1003', '46.44070602', '8165'], ['-111', '51', '340', '1001', '44.73457671', '8230'], ['-111', '52', '340', '999', '69.7314626', '4428'], ['-111', '53', '338', '997', '65.99422335', '5805'], ['-109', '55', '338', '1002', '36.6420946', '5354'], ['-108', '58', '337', '995', '32.34733303', '3395'], ['-103', '59', '336', '1003', '36.27946969', '8274'], ['-101', '62', '336', '997', '54.9910141', '-333'], ['-100', '63', '335', '998', '57.45493831', '5064'], ['-99', '64', '331', '996', '48.07939353', '357'], ['-99', '65', '330', '1004', '41.47051398', '4793'], ['-97', '65', '328', '1004', '40.83334811', '2423'], ['-96', '67', '328', '995', '60.33915071', '132'], ['-95', '67', '326', '1002', '64.84653329', '2080'], ['-95', '69', '326', '1000', '46.42125006', '8990'], ['-94', '70', '325', '1001', '53.92669255', '1868'], ['-93', '72', '324', '1003', '51.26641653', '2628'], ['-91', '76', '324', '998', '68.31971927', '5689'], ['-90', '76', '323', '996', '33.34594833', '4999'], ['-89', '77', '323', '999', '48.78909613', '2635'], ['-89', '77', '319', '997', '65.47889859', '6261'], ['-88', '77', '316', '1003', '45.99694669', '2159'], ['-87', '79', '314', '1001', '59.65839161', '3212'], ['-87', '80', '311', '1000', '54.75993727', '4338'], ['-87', '80', '310', '998', '44.67930268', '6569'], ['-87', '81', '309', '997', '42.49654495', '3831'], ['-87', '81', '307', '1002', '40.34567832', '1677'], ['-86', '82', '306', '999', '66.10166083', '4094'], ['-84', '83', '305', '995', '49.27216206', '4263'], ['-83', '85', '304', '997', '49.38082489', '1569'], ['-82', '87', '302', '996', '49.25375355', '457'], ['-81', '90', '301', '1000', '47.24874383', '8518'], ['-78', '90', '301', '1000', '32.48683302', '674'], ['-77', '93', '300', '1001', '40.74291978', '2304'], ['-77', '93', '298', '1000', '59.8815223', '3178'], ['-76', '96', '298', '1003', '54.98440051', '2817'], ['-74', '97', '297', '1003', '41.20101996', '507'], ['-74', '99', '297', '999', '34.63017694', 
'6783'], ['-68', '101', '295', '998', '56.84518776', '2654'], ['-67', '101', '295', '997', '62.02433813', '7981'], ['-64', '103', '291', '1004', '66.37736476', '8477'], ['-63', '105', '291', '995', '67.38739104', '7224'], ['-61', '106', '290', '1000', '41.73885919', '6367'], ['-61', '106', '289', '1001', '32.52842727', '1576'], ['-60', '107', '286', '1003', '31.0586949', '8324'], ['-60', '108', '283', '999', '30.60381835', '1931'], ['-59', '110', '281', 
'1000', '41.26204089', '6814'], ['-58', '111', '279', '995', '64.44837079', '3113'], ['-58', '112', '278', '996', '39.73842692', '5168'], ['-57', '112', '274', '998', '58.96099032', '7588'], ['-57', '113', '270', '995', '60.29573035', '500'], ['-57', '115', '267', '997', '52.54848034', '1514'], ['-56', '116', '266', '995', '42.2787071', '5369'], ['-56', '117', '265', '1004', '63.38082144', '7401'], ['-55', '120', '263', '997', '47.16607022', '2746'], ['-55', '122', '263', '1000', '53.90662434', '4421'], ['-54', '122', '263', '995', '56.06957706', '646'], ['-54', '124', '262', '1000', '64.21954837', '282'], ['-53', '125', '261', '995', '35.57610178', '4631'], ['-53', '127', '261', '997', '35.46068713', '4142'], ['-50', '128', '261', '1002', '39.37180447', '8624'], ['-50', '129', '260', '1003', '35.3940564', '7099'], ['-47', '131', '258', '997', '40.62207275', '7009'], ['-45', '133', '257', '1004', '40.31493534', '6079'], ['-45', '135', '257', '997', '48.17300603', '7511'], ['-44', '141', '256', '999', '60.90720558', '5786'], ['-42', '143', '256', '998', '48.95165499', '6325'], ['-41', '144', '253', '996', '42.43287262', '1981'], ['-41', '144', '251', '1002', '46.51204291', '5757'], ['-41', '145', '249', '995', '62.72022118', '955'], ['-39', '145', '248', '1001', '67.82667941', '4846'], ['-37', '145', '247', '996', '60.14939951', '7955'], ['-37', '146', 
'246', '1002', '56.57621333', '2702'], ['-36', '146', '245', '1003', '51.21912996', '7255'], ['-33', '146', '245', '996', '41.38534274', '-21'], ['-31', '148', '245', '996', '36.48449368', '2250'], ['-30', '149', '244', '1003', '69.03472352', '1428'], ['-26', '150', '243', '999', '67.1530376', '2998'], ['-26', '150', '241', '1004', '60.02881675', '3293'], ['-24', '153', '240', '1003', '45.30302124', '7521'], ['-23', '153', '239', '998', '33.19097345', '6451'], ['-21', '154', '234', '1002', '55.53720884', '7622'], ['-21', '156', '230', '1004', '42.29023734', '3925'], ['-20', '157', '229', '995', '55.06805584', '2748'], ['-19', '160', '229', '1000', '43.07530753', '4207'], ['-19', '160', '228', '999', '57.45654908', '7077'], ['-18', '163', '227', '1004', '59.20667843', '636'], ['-17', '164', '227', '1004', '64.70937456', '8453'], ['-17', '167', '227', '999', '31.74741353', '765'], ['-16', '167', '224', '999', '35.20529841', '2592'], ['-13', '168', '224', '996', '35.40901545', '3740'], ['-13', '171', '221', '1000', '66.53922122', '1034'], ['-12', '171', '219', '1001', '64.34232317', '3284'], ['-11', '172', '218', '995', '53.69005867', '2817'], ['-11', '172', '218', '996', '40.86128458', '5792'], ['-11', '174', '216', '997', '49.37079172', '3272'], ['-10', '174', '211', '997', '35.41764951', '6420'], ['-10', '175', '208', '1004', '45.93159524', '777'], ['-9', '175', '207', '1003', '44.64809597', '5491'], ['-8', '177', '206', '996', '30.78676566', '6303'], ['-7', '180', '205', '998', '56.40476813', '4493'], ['-6', '181', '204', '995', '32.72590008', '2063'], ['-6', '182', '204', '1001', '40.08153425', '7201'], ['-3', '182', '203', '1001', '56.02035629', '1142'], ['0', '184', '202', '1003', '68.37872812', '3189'], ['1', '186', '201', '998', '43.86244287', '8833'], ['2', '187', '199', '1002', '66.08664469', 
'4592'], ['3', '188', '199', '1003', '36.67962374', '255'], ['3', '189', '198', '1004', '61.25253348', '2011'], ['4', '189', '198', '999', '39.16909982', '7265'], ['7', '190', '197', '1004', '35.48142904', '2028'], ['8', '190', '195', '1001', '65.2211191', '1860'], ['9', '190', '194', '997', '65.82594789', '5607'], ['9', '191', '192', '997', '32.74373126', '8908'], ['10', '192', '191', '1002', '59.49691411', '3526'], ['12', '194', '190', '999', '62.46698675', '3547'], ['13', '195', '190', '1001', '40.37107202', '318'], ['14', '197', '190', '996', '60.73712679', '8484'], ['16', '198', '189', '998', '61.89849144', '6034'], ['16', '198', '189', '995', '55.97987457', '5712'], ['17', '199', '188', '998', '45.18688251', '4251'], ['17', '199', '187', '995', '54.32149605', '6761'], ['18', '201', '186', '1003', '63.84544301', '6276'], ['18', '202', '184', '1000', '67.53552319', '3824'], ['18', '203', '182', '999', '44.60072283', '-39'], ['19', '204', '182', '1000', '31.87966685', '3088'], ['20', '204', '181', '1002', '58.00887881', '8509'], ['20', '205', '180', '1000', '56.19498751', '146'], ['21', '206', '177', '1004', '38.30402195', '3484'], ['21', '207', '175', '999', '47.29251428', '2635'], ['23', '208', '175', '1004', '53.03346427', '5863'], ['24', '211', '174', '1000', '49.87480198', '8133'], ['24', '216', '174', '997', '65.17631791', '1496'], ['26', '218', '172', '995', '65.77835398', '1343'], ['26', '218', '172', '995', '69.21714765', '7621'], ['26', '219', '171', '1002', '53.20548344', '93'], ['26', '221', '171', '1004', '43.74172602', '3060'], ['26', '224', '168', '1004', '48.92089285', '967'], ['27', '224', '167', '1004', '37.63999189', '8580'], ['27', '227', '167', '1004', '57.64151551', '7315'], ['29', '227', '164', '1000', '45.55046613', '5723'], ['29', '227', '163', '1000', '66.84871459', '2888'], ['29', '228', '160', '997', '46.99887632', '4737'], ['31', '229', '160', '1004', '33.07662846', '7192'], ['31', '229', '157', '1000', '60.05749122', '1538'], ['32', '230', '156', '999', '48.09862181', '6749'], ['32', '234', '154', '998', '67.95163614', '4329'], ['32', '239', '153', '997', '48.46713368', '7258'], ['32', '240', '153', '1001', '37.96519934', '5412'], ['34', '241', '150', '1001', '68.09901458', '3789'], ['36', '243', '150', '996', '46.27213704', '702'], ['38', '244', '149', '1003', '42.5855702', '993'], ['38', '245', '148', '1001', '44.68884753', '4958'], ['39', '245', '146', '1002', '61.77914665', '-290'], ['41', '245', '146', '996', '36.65091449', '2104'], ['43', '246', '146', '997', '66.75588711', '4042'], ['44', '247', '145', '1002', '40.10730646', '7618'], ['44', '248', '145', '1004', '48.10491982', '6725'], ['45', '249', '145', '1003', '62.84488224', '-147'], ['45', '251', '144', '999', '60.57582709', '-362'], ['47', '253', '144', '997', '59.25034782', '2800'], ['48', '256', '143', '1001', '42.35519235', '3459'], ['48', '256', '141', '999', '65.68580984', '6469'], ['49', '257', '135', '997', '41.31910469', '8621'], ['50', '257', '133', '1001', '38.86949737', '4543'], ['52', '258', '131', '997', '41.36013752', '1308'], ['52', '260', '129', '997', '66.55623715', '1016'], ['54', '261', '128', '1000', '32.51373357', '5364'], ['54', '261', '127', '1000', '48.38177365', '3550'], ['55', '261', '125', '1003', '56.87188062', '1327'], ['58', '262', '124', '1000', '39.84737475', '1704'], ['59', '263', '122', '999', '35.27882281', '6451'], ['60', '263', '122', '1000', '46.23025436', '1497'], ['61', '263', '120', '1003', '65.36516444', '3594'], ['61', '265', '117', '1001', '39.73342885', '4200'], ['62', '266', '116', '996', '68.62940801', '1595'], ['64', '267', '115', '999', '31.65948591', '3905'], ['64', '270', '113', '998', '44.07031673', '3893'], ['65', '274', '112', '1002', '59.64380378', '6486'], ['68', '278', '112', '995', '51.40282221', '2774'], ['71', '279', '111', '998', '62.68102529', '3746'], ['73', '281', '110', '1003', '53.62151186', '4213'], ['74', '283', '108', '997', '37.90224298', '4284'], ['74', '286', '107', '1002', '47.28057512', '7838'], ['76', '289', '106', '1001', '69.68774035', '3775'], ['78', '290', '106', '996', '48.31344797', '3238'], ['78', '291', '105', '1001', '44.57063624', '2979'], ['78', '291', '103', '1004', '60.66890814', '254'], ['79', '295', '101', '1002', '51.12322664', '3357'], ['79', '295', '101', '996', '54.2929619', '6073'], ['79', '297', '99', '999', '59.25282198', '2209'], ['79', '297', '97', '998', '50.88532577', '-46'], ['80', '298', '96', '1002', '43.19853935', '8312'], ['80', '298', '93', '995', '57.86340756', '3298'], ['81', '300', '93', '1001', '34.93972355', '2505'], ['82', '301', '90', '1003', '59.16966106', '769'], ['82', '301', '90', '1004', '58.54300226', '4761'], ['82', '302', '87', '997', '51.8623969', '2277'], ['83', '304', '85', '998', '45.94540666', '3333'], ['83', '305', '83', '998', '43.26030152', '5302'], ['87', '306', '82', '1001', '42.48048519', '4090'], ['87', '307', '81', '995', '53.04087915', '1715'], ['87', '309', '81', '1002', '44.41655503', '7873'], ['88', '310', '80', 
'997', '62.85638168', '3081'], ['90', '311', '80', '996', '67.26449809', '8527'], ['92', '314', '79', '997', '34.56941349', '-259'], ['92', '316', '77', '1000', '49.37908301', '3169'], ['95', '319', '77', '996', '35.00208909', '819'], ['95', '323', '77', '1003', '46.5275499', '2257'], ['96', '323', '76', '998', '63.36613142', '6698'], ['96', '324', '76', '1004', '55.28279651', '1472'], ['96', '324', '72', '997', '37.47390324', '5762'], ['97', '325', '70', '999', '54.53442559', '5952'], ['98', '326', '69', '1004', '53.1468931', '5668'], ['99', '326', '67', '995', '50.59033891', '937'], ['99', '328', '67', '1001', '36.83869436', '4511'], ['99', '328', '65', '1004', '65.40986844', 
'-34'], ['100', '330', '65', '996', '52.88046226', '5753'], ['100', '331', '64', '1004', '55.60800236', '8436'], ['101', '335', '63', '1001', '37.06800259', '2385'], ['102', '336', '62', '1000', '50.35322481', '8527'], ['104', '336', '59', '1002', '57.24309023', '2926'], ['104', '337', '58', '996', '34.78715619', '7627'], ['106', '338', '55', '996', '42.84243156', '-286'], ['106', '338', '53', '1004', '61.54862119', '2719'], ['107', '340', '52', '1003', 
'61.7206165', '8616'], ['107', '340', '51', '1001', '62.26711425', '5336'], ['108', '341', '50', '996', '56.76840666', '1733'], ['109', '342', '50', '1000', '69.38976726', '4277'], ['110', '342', '48', '1001', '53.52780269', '7830'], ['111', '343', '47', '1002', '60.75602977', '808'], ['113', '343', '45', '997', '50.8436813', '7702'], ['114', '344', '43', '998', '66.38470881', '4234'], ['114', '347', '43', '995', '52.90765358', '5728'], ['114', '349', '41', '1004', '66.83937736', '1528'], ['115', '350', '40', '1002', '40.48010853', '4449'], ['115', '352', '37', '998', '43.85139347', '157'], ['116', '353', '36', '997', '58.94046817', '2245'], ['117', '356', '32', '1003', '68.31248794', '1828'], ['118', '357', '31', '1002', '59.59613981', '5626'], ['119', '359', '28', '1003', '36.65515813', '8785'], ['123', '359', '27', '1003', '38.24435868', '7590'], ['124', '360', '26', '1004', '49.96886059', '5697'], ['126', '360', '26', '996', '35.03041083', '234'], ['127', '361', '25', '1003', '59.04094013', '744'], ['127', '362', '22', '1004', '69.63820569', '5512'], ['128', '364', '21', '1000', '59.43772427', '7310'], ['128', '367', '21', 
'1001', '43.80606886', '5794'], ['129', '371', '21', '1002', '69.84177774', '2761'], ['132', '373', '21', '1000', '63.26383105', '6261'], ['132', '374', '20', '995', '41.41261975', '2065'], ['135', '375', '20', '1003', '65.86109695', '5457'], ['135', '376', '18', '995', '70.28657005', '3327'], ['136', '377', '17', '999', '61.45420064', '1436'], ['136', '379', '16', '998', '69.81162019', '8596'], ['137', '386', '11', '996', '53.37655985', '8421'], ['139', '387', '11', '1003', '56.19552764', '5310'], ['139', '393', '11', '995', '39.71293991', '-322'], ['140', '393', '8', '995', '47.77708878', '3625'], ['141', '395', '7', '998', '61.319663', '8446'], ['144', '395', '6', '995', '58.69343634', '3260'], ['151', '395', '5', '998', '66.97528407', '2690'], ['153', '397', '5', '998', '44.29079642', '2700'], ['154', '397', '2', '1002', '61.13607295', '1098']]

with open("artificial_dataset.csv", 'w', newline='') as file_name: 
    file_write = csv.writer(file_name)
    file_write.writerows(array)
    file_name.write