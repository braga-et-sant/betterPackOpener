import os


def main(d, banlistfolder, banlistname, whitelist):
    """
    Makes a banlist file using the dictionary created from one of the previous 2 helper functions
    (Those being buildRestrict and buildWhitelist)
    :param d: Dict, the aforementioned dictionary
    :param banlistname: String, The name of the new file
    :param whitelist: Boolean, Whether the banlist is a whitelist or not.
    """

    if (whitelist):
        banlistname = "Whitelist" + banlistname
    if os.path.isdir(banlistfolder):
        try:
            with open(banlistfolder + '/' + banlistname + ".lflist.CONF", "x") as f:
                f.write("#[" + banlistname + "]" + "\n")
                f.write("!" + banlistname + "\n")
                if (whitelist):
                    f.write("$whitelist\n")
                for key, value in d.items():
                    f.write(key + " " + str(value[1]) + " -" + value[0] + "\n")

                if (whitelist):
                    # Removing extra cards
                    samenamecards = ["22702055", "26534688", "74335036", "34103656", "2819435", "91932350", "27927359",
                                     "54415063", "80316585"]
                    animeexclusive = ["511000566", "511000572", "513000053", "511020012", "511002048", "513000001",
                                      "511000559", "511002613", "511000574", "511002616", "160403001", "511002614",
                                      "511009557", "511000567", "511002049", "511001128", "160001015", "511003075",
                                      "511009564", "511000568", "511002513", "511003056", "511019009", "511019001",
                                      "511600239", "511019002", "511019003", "160001012", "511009331", "511002828",
                                      "160001002", "511001595", "160001010", "160001001", "160001008", "160001009",
                                      "513000030", "511002418", "513000028", "513000029", "513000095", "511000378",
                                      "511002501", "511004006", "511000695", "511000769", "511002506", "511002507",
                                      "511002508", "511000539", "511600061", "511000565", "511600100", "511600166",
                                      "810000114", "511001147", "511000560", "511000570", "511002504", "511000562",
                                      "511010701", "511004015", "511015127", "511002127", "511600189", "511310000",
                                      "511000575", "810000028", "513000142", "511005647", "511000573", "511000569",
                                      "511002167", "511000564", "511009014", "511600169", "511756001", "511600069",
                                      "511002500", "511600193", "511000772", "511001040", "160404002", "511000563",
                                      "511002854", "511018019", "511000590", "511000462", "511001057", "511018028",
                                      "511000477", "511002533", "511000571", "511000591", "511000240", "160001040",
                                      "160001042", "160001043", "160404003", "511000218", "511000474", "511000548",
                                      "511001126", "511001651", "511002057", "511002295", "511002403", "511002415",
                                      "511002531", "511002540", "511002549", "511002825", "511008009", "511018004",
                                      "511021008", "511600096", "511600170", "511777003", "511777009", "513000054",
                                      "513000055", "513000116", "511000241", "511000373", "511000377", "511000541",
                                      "511000604", "511002523", "511002539", "511004341", "511005063", "511600004",
                                      "511600290", "511000258", "511002461", "511002578", "511004007", "511010700",
                                      "511002499", "810000042", "810000043", "26534688", "160001045", "160001048",
                                      "511000278", "511000475", "511000987", "511001122", "511002446", "511002884",
                                      "511005091", "511020009", "511600062", "810000055", "511000248", "511001016",
                                      "511001887", "511002444", "513000002", "513000026", "513000066", "513000111",
                                      "511013024", "511003023", "511001594", "511001599", "511001211", "810000011",
                                      "511024001", "511600286", "511001600", "511000613", "511000540", "511002541",
                                      "511002776", "511600038", "511002542", "511002379", "511310007", "511756003",
                                      "511003058", "511002617", "511004004", "511000246", "511000261", "511000234",
                                      "511015128", "511002835", "511023008"]

                    rushexclusive = ["160406009", "160003011", "160406001", "160406002", "160003010", "160001011",
                                     "160003008", "160004011", "160002004", "160003007", "160003006", "160003005",
                                     "160002014", "160406006", "160002040", "160002041", "160002044", "160201011",
                                     "160201001", "160406010", "160411002", "160003052", "160003053", "160005054",
                                     "160002050", ]

                    for code in samenamecards:
                        if not code in d:
                            f.write(code + " -1 - " + "umiclone" + "\n")
                    for code in animeexclusive:
                        f.write(code + " -1 - " + "anime card" + "\n")
                    for code in rushexclusive:
                        f.write(code + " -1 - " + "rush card" + "\n")
        except FileExistsError:
            print("Error, file already exists. Aborting print")
