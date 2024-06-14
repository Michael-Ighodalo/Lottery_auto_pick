# Install the following list:
# selenium, webdriver_manager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

first_quarter = ["000", "001", "002", "003", "004", "005", "006", "007", "008", "009", "010", "011", "012", "013", "014", "015", "016", "017", "018", "019", "020", "021", "022", "023", "024", "025", "026", "027", "028", "029", "030", "031", "032", "033", "034", "035", "036", "037", "038", "039", "040", "041", "042", "043", "044", "045", "046", "047", "048", "049", "050", "051", "052", "053", "054", "055", "056", "057", "058", "059", "060", "061", "062", "063", "064", "065", "066", "067", "068", "069", "070", "071", "072", "073", "074", "075", "076", "077", "078", "079", "080", "081", "082", "083", "084", "085", "086", "087", "088", "089", "090", "091", "092", "093", "094", "095", "096", "097", "098", "099", "100", "101", "102", "103", "104", "105", "106", "107", "108", "109", "110", "111", "112", "113", "114", "115", "116", "117", "118", "119", "120", "121", "122", "123", "124", "125", "126", "127", "128", "129", "130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "140", "141", "142", "143", "144", "145", "146", "147", "148", "149", "150", "151", "152", "153", "154", "155", "156", "157", "158", "159", "160", "161", "162", "163", "164", "165", "166", "167", "168", "169", "170", "171", "172", "173", "174", "175", "176", "177", "178", "179", "180", "181", "182", "183", "184", "185", "186", "187", "188", "189", "190", "191", "192", "193", "194", "195", "196", "197", "198", "199", "200", "201", "202", "203", "204", "205", "206", "207", "208", "209", "210", "211", "212", "213", "214", "215", "216", "217", "218", "219", "220", "221", "222", "223", "224", "225", "226", "227", "228", "229", "230", "231", "232", "233", "234", "235", "236", "237", "238", "239", "240", "241", "242", "243", "244", "245", "246", "247", "248", "249", "250"]
second_quarter = ["251", "252", "253", "254", "255", "256", "257", "258", "259", "260", "261", "262", "263", "264", "265", "266", "267", "268", "269", "270", "271", "272", "273", "274", "275", "276", "277", "278", "279", "280", "281", "282", "283", "284", "285", "286", "287", "288", "289", "290", "291", "292", "293", "294", "295", "296", "297", "298", "299", "300", "301", "302", "303", "304", "305", "306", "307", "308", "309", "310", "311", "312", "313", "314", "315", "316", "317", "318", "319", "320", "321", "322", "323", "324", "325", "326", "327", "328", "329", "330", "331", "332", "333", "334", "335", "336", "337", "338", "339", "340", "341", "342", "343", "344", "345", "346", "347", "348", "349", "350", "351", "352", "353", "354", "355", "356", "357", "358", "359", "360", "361", "362", "363", "364", "365", "366", "367", "368", "369", "370", "371", "372", "373", "374", "375", "376", "377", "378", "379", "380", "381", "382", "383", "384", "385", "386", "387", "388", "389", "390", "391", "392", "393", "394", "395", "396", "397", "398", "399", "400", "401", "402", "403", "404", "405", "406", "407", "408", "409", "410", "411", "412", "413", "414", "415", "416", "417", "418", "419", "420", "421", "422", "423", "424", "425", "426", "427", "428", "429", "430", "431", "432", "433", "434", "435", "436", "437", "438", "439", "440", "441", "442", "443", "444", "445", "446", "447", "448", "449", "450", "451", "452", "453", "454", "455", "456", "457", "458", "459", "460", "461", "462", "463", "464", "465", "466", "467", "468", "469", "470", "471", "472", "473", "474", "475", "476", "477", "478", "479", "480", "481", "482", "483", "484", "485", "486", "487", "488", "489", "490", "491", "492", "493", "494", "495", "496", "497", "498", "499", "500"]
third_quarter = ["501", "502", "503", "504", "505", "506", "507", "508", "509", "510", "511", "512", "513", "514", "515", "516", "517", "518", "519", "520", "521", "522", "523", "524", "525", "526", "527", "528", "529", "530", "531", "532", "533", "534", "535", "536", "537", "538", "539", "540", "541", "542", "543", "544", "545", "546", "547", "548", "549", "550", "551", "552", "553", "554", "555", "556", "557", "558", "559", "560", "561", "562", "563", "564", "565", "566", "567", "568", "569", "570", "571", "572", "573", "574", "575", "576", "577", "578", "579", "580", "581", "582", "583", "584", "585", "586", "587", "588", "589", "590", "591", "592", "593", "594", "595", "596", "597", "598", "599", "600", "601", "602", "603", "604", "605", "606", "607", "608", "609", "610", "611", "612", "613", "614", "615", "616", "617", "618", "619", "620", "621", "622", "623", "624", "625", "626", "627", "628", "629", "630", "631", "632", "633", "634", "635", "636", "637", "638", "639", "640", "641", "642", "643", "644", "645", "646", "647", "648", "649", "650", "651", "652", "653", "654", "655", "656", "657", "658", "659", "660", "661", "662", "663", "664", "665", "666", "667", "668", "669", "670", "671", "672", "673", "674", "675", "676", "677", "678", "679", "680", "681", "682", "683", "684", "685", "686", "687", "688", "689", "690", "691", "692", "693", "694", "695", "696", "697", "698", "699", "700", "701", "702", "703", "704", "705", "706", "707", "708", "709", "710", "711", "712", "713", "714", "715", "716", "717", "718", "719", "720", "721", "722", "723", "724", "725", "726", "727", "728", "729", "730", "731", "732", "733", "734", "735", "736", "737", "738", "739", "740", "741", "742", "743", "744", "745", "746", "747", "748", "749", "750"]
fourth_quarter = ["751", "752", "753", "754", "755", "756", "757", "758", "759", "760", "761", "762", "763", "764", "765", "766", "767", "768", "769", "770", "771", "772", "773", "774", "775", "776", "777", "778", "779", "780", "781", "782", "783", "784", "785", "786", "787", "788", "789", "790", "791", "792", "793", "794", "795", "796", "797", "798", "799", "800", "801", "802", "803", "804", "805", "806", "807", "808", "809", "810", "811", "812", "813", "814", "815", "816", "817", "818", "819", "820", "821", "822", "823", "824", "825", "826", "827", "828", "829", "830", "831", "832", "833", "834", "835", "836", "837", "838", "839", "840", "841", "842", "843", "844", "845", "846", "847", "848", "849", "850", "851", "852", "853", "854", "855", "856", "857", "858", "859", "860", "861", "862", "863", "864", "865", "866", "867", "868", "869", "870", "871", "872", "873", "874", "875", "876", "877", "878", "879", "880", "881", "882", "883", "884", "885", "886", "887", "888", "889", "890", "891", "892", "893", "894", "895", "896", "897", "898", "899", "900", "901", "902", "903", "904", "905", "906", "907", "908", "909", "910", "911", "912", "913", "914", "915", "916", "917", "918", "919", "920", "921", "922", "923", "924", "925", "926", "927", "928", "929", "930", "931", "932", "933", "934", "935", "936", "937", "938", "939", "940", "941", "942", "943", "944", "945", "946", "947", "948", "949", "950", "951", "952", "953", "954", "955", "956", "957", "958", "959", "960", "961", "962", "963", "964", "965", "966", "967", "968", "969", "970", "971", "972", "973", "974", "975", "976", "977", "978", "979", "980", "981", "982", "983", "984", "985", "986", "987", "988", "989", "990", "991", "992", "993", "994", "995", "996", "997", "998", "999"]
randy_run = ["980", "981", "982", "983", "984", "985", "986", "987", "988", "989", "990", "991", "992", "993", "994", "995", "996", "997", "998", "999"]

# to make the browser stay open after process or close it.
options = Options()
options.add_experimental_option("detach", True)
# True is opened browser after process
# False is close browser after process
# -----------------------------------------------------------------
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)
# This line below opens browser in incognito mode
# options.add_argument("--incognito")

driver.get("https://nationallotterynigeria.com/pick3")
driver.maximize_window()

# Click sign up, now bro to get the xpath for straight forward link clicks ba
# go to chrome site, highlight element and inspect, then on that line of script
# right click, copy select, then copy xpath, remember to change the "" to "" inside the xpath
links = driver.find_elements("xpath", "//*[@id='root']/div/header/div/div/div[1]/a[1]")
for link in links:
    print(link.get_attribute("innerHTML"))
    link.click()

phone_number = driver.find_elements("xpath", "//*[@id='root']/div/div[1]/div/div[2]/div/form/div[1]/div/input")
for number in phone_number:
    number.click()
    number.send_keys("8133758030")

password = driver.find_elements("xpath", "//*[@id='root']/div/div[1]/div/div[2]/div/form/div[2]/input")
for pwd in password:
    pwd.click()
    pwd.send_keys("Mykael46.")

signup = driver.find_elements("xpath", "//*[@id='root']/div/div[1]/div/div[2]/div/form/div[3]/button")
for sign_in in signup:
    sign_in.click()

play_now = driver.find_elements("xpath", "//*[@id='root']/div/div[1]/div/div[3]/button")
for play in play_now:
    play.click()

zero_1 = "//*[@id='root']/div/div[2]/div[3]/div[2]/div[1]/div/div[1]/span"
one_1 = "//*[@id='root']/div/div[2]/div[3]/div[2]/div[1]/div/div[2]/span"
two_1 = "//*[@id='root']/div/div[2]/div[3]/div[2]/div[1]/div/div[3]/span"
three_1 = "//*[@id='root']/div/div[2]/div[3]/div[2]/div[1]/div/div[4]/span"
four_1 = "//*[@id='root']/div/div[2]/div[3]/div[2]/div[1]/div/div[5]/span"
five_1 = "//*[@id='root']/div/div[2]/div[3]/div[2]/div[1]/div/div[6]/span"
six_1 = "//*[@id='root']/div/div[2]/div[3]/div[2]/div[1]/div/div[7]/span"
seven_1 = "//*[@id='root']/div/div[2]/div[3]/div[2]/div[1]/div/div[8]/span"
eight_1 = "//*[@id='root']/div/div[2]/div[3]/div[2]/div[1]/div/div[9]/span"
nine_1 = "//*[@id='root']/div/div[2]/div[3]/div[2]/div[1]/div/div[10]/span"

zero_2 = "//*[@id='root']/div/div[2]/div[3]/div[2]/div[2]/div/div[1]/span"
one_2 = "//*[@id='root']/div/div[2]/div[3]/div[2]/div[2]/div/div[2]/span"
two_2 = "//*[@id='root']/div/div[2]/div[3]/div[2]/div[2]/div/div[3]/span"
three_2 = "//*[@id='root']/div/div[2]/div[3]/div[2]/div[2]/div/div[4]/span"
four_2 = "//*[@id='root']/div/div[2]/div[3]/div[2]/div[2]/div/div[5]/span"
five_2 = "//*[@id='root']/div/div[2]/div[3]/div[2]/div[2]/div/div[6]/span"
six_2 = "//*[@id='root']/div/div[2]/div[3]/div[2]/div[2]/div/div[7]/span"
seven_2 = "//*[@id='root']/div/div[2]/div[3]/div[2]/div[2]/div/div[8]/span"
eight_2 = "//*[@id='root']/div/div[2]/div[3]/div[2]/div[2]/div/div[9]/span"
nine_2 = "//*[@id='root']/div/div[2]/div[3]/div[2]/div[2]/div/div[10]/span"

zero_3 = "//*[@id='root']/div/div[2]/div[3]/div[2]/div[3]/div/div[1]/span"
one_3 = "//*[@id='root']/div/div[2]/div[3]/div[2]/div[3]/div/div[2]/span"
two_3 = "//*[@id='root']/div/div[2]/div[3]/div[2]/div[3]/div/div[3]/span"
three_3 = "//*[@id='root']/div/div[2]/div[3]/div[2]/div[3]/div/div[4]/span"
four_3 = "//*[@id='root']/div/div[2]/div[3]/div[2]/div[3]/div/div[5]/span"
five_3 = "//*[@id='root']/div/div[2]/div[3]/div[2]/div[3]/div/div[6]/span"
six_3 = "//*[@id='root']/div/div[2]/div[3]/div[2]/div[3]/div/div[7]/span"
seven_3 = "//*[@id='root']/div/div[2]/div[3]/div[2]/div[3]/div/div[8]/span"
eight_3 = "//*[@id='root']/div/div[2]/div[3]/div[2]/div[3]/div/div[9]/span"
nine_3 = "//*[@id='root']/div/div[2]/div[3]/div[2]/div[3]/div/div[10]/span"

first_question = input("Should I do first? y/n")
if first_question == "y":
    for a in first_quarter:
        if a[0] == "0":
            first_value = driver.find_elements("xpath", zero_1)
            for val_first in first_value:
                val_first.click()
        if a[0] == "1":
            first_value = driver.find_elements("xpath", one_1)
            for val_first in first_value:
                val_first.click()
        if a[0] == "2":
            first_value = driver.find_elements("xpath", two_1)
            for val_first in first_value:
                val_first.click()
        if a[0] == "3":
            first_value = driver.find_elements("xpath", three_1)
            for val_first in first_value:
                val_first.click()
        if a[0] == "4":
            first_value = driver.find_elements("xpath", four_1)
            for val_first in first_value:
                val_first.click()
        if a[0] == "5":
            first_value = driver.find_elements("xpath", five_1)
            for val_first in first_value:
                val_first.click()
        if a[0] == "6":
            first_value = driver.find_elements("xpath", six_1)
            for val_first in first_value:
                val_first.click()
        if a[0] == "7":
            first_value = driver.find_elements("xpath", seven_1)
            for val_first in first_value:
                val_first.click()
        if a[0] == "8":
            first_value = driver.find_elements("xpath", eight_1)
            for val_first in first_value:
                val_first.click()
        if a[0] == "9":
            first_value = driver.find_elements("xpath", nine_1)
            for val_first in first_value:
                val_first.click()
        if a[1] == "0":
            second_value = driver.find_elements("xpath", zero_2)
            for val_second in second_value:
                val_second.click()
        if a[1] == "1":
            second_value = driver.find_elements("xpath", one_2)
            for val_second in second_value:
                val_second.click()
        if a[1] == "2":
            second_value = driver.find_elements("xpath", two_2)
            for val_second in second_value:
                val_second.click()
        if a[1] == "3":
            second_value = driver.find_elements("xpath", three_2)
            for val_second in second_value:
                val_second.click()
        if a[1] == "4":
            second_value = driver.find_elements("xpath", four_2)
            for val_second in second_value:
                val_second.click()
        if a[1] == "5":
            second_value = driver.find_elements("xpath", five_2)
            for val_second in second_value:
                val_second.click()
        if a[1] == "6":
            second_value = driver.find_elements("xpath", six_2)
            for val_second in second_value:
                val_second.click()
        if a[1] == "7":
            second_value = driver.find_elements("xpath", seven_2)
            for val_second in second_value:
                val_second.click()
        if a[1] == "8":
            second_value = driver.find_elements("xpath", eight_2)
            for val_second in second_value:
                val_second.click()
        if a[1] == "9":
            second_value = driver.find_elements("xpath", nine_2)
            for val_second in second_value:
                val_second.click()
        if a[2] == "0":
            third_value = driver.find_elements("xpath", zero_3)
            for val_third in third_value:
                val_third.click()
        if a[2] == "1":
            third_value = driver.find_elements("xpath", one_3)
            for val_third in third_value:
                val_third.click()
        if a[2] == "2":
            third_value = driver.find_elements("xpath", two_3)
            for val_third in third_value:
                val_third.click()
        if a[2] == "3":
            third_value = driver.find_elements("xpath", three_3)
            for val_third in third_value:
                val_third.click()
        if a[2] == "4":
            third_value = driver.find_elements("xpath", four_3)
            for val_third in third_value:
                val_third.click()
        if a[2] == "5":
            third_value = driver.find_elements("xpath", five_3)
            for val_third in third_value:
                val_third.click()
        if a[2] == "6":
            third_value = driver.find_elements("xpath", six_3)
            for val_third in third_value:
                val_third.click()
        if a[2] == "7":
            third_value = driver.find_elements("xpath", seven_3)
            for val_third in third_value:
                val_third.click()
        if a[2] == "8":
            third_value = driver.find_elements("xpath", eight_3)
            for val_third in third_value:
                val_third.click()
        if a[2] == "9":
            third_value = driver.find_elements("xpath", nine_3)
            for val_third in third_value:
                val_third.click()
        else:
            print("something happened")
        print(a)

        submit = driver.find_elements("xpath", "//*[@id='root']/div/div[2]/div[3]/button")
        for submitting in submit:
            submitting.click()

if first_question == "n":
    print("aight, so no 000 to 250, cool, buh its logical though")

second_question = input("Should I do second? y/n")
if second_question == "y":
    for a in second_quarter:
        if a[0] == "0":
            first_value = driver.find_elements("xpath", zero_1)
            for val_first in first_value:
                val_first.click()
        if a[0] == "1":
            first_value = driver.find_elements("xpath", one_1)
            for val_first in first_value:
                val_first.click()
        if a[0] == "2":
            first_value = driver.find_elements("xpath", two_1)
            for val_first in first_value:
                val_first.click()
        if a[0] == "3":
            first_value = driver.find_elements("xpath", three_1)
            for val_first in first_value:
                val_first.click()
        if a[0] == "4":
            first_value = driver.find_elements("xpath", four_1)
            for val_first in first_value:
                val_first.click()
        if a[0] == "5":
            first_value = driver.find_elements("xpath", five_1)
            for val_first in first_value:
                val_first.click()
        if a[0] == "6":
            first_value = driver.find_elements("xpath", six_1)
            for val_first in first_value:
                val_first.click()
        if a[0] == "7":
            first_value = driver.find_elements("xpath", seven_1)
            for val_first in first_value:
                val_first.click()
        if a[0] == "8":
            first_value = driver.find_elements("xpath", eight_1)
            for val_first in first_value:
                val_first.click()
        if a[0] == "9":
            first_value = driver.find_elements("xpath", nine_1)
            for val_first in first_value:
                val_first.click()
        if a[1] == "0":
            second_value = driver.find_elements("xpath", zero_2)
            for val_second in second_value:
                val_second.click()
        if a[1] == "1":
            second_value = driver.find_elements("xpath", one_2)
            for val_second in second_value:
                val_second.click()
        if a[1] == "2":
            second_value = driver.find_elements("xpath", two_2)
            for val_second in second_value:
                val_second.click()
        if a[1] == "3":
            second_value = driver.find_elements("xpath", three_2)
            for val_second in second_value:
                val_second.click()
        if a[1] == "4":
            second_value = driver.find_elements("xpath", four_2)
            for val_second in second_value:
                val_second.click()
        if a[1] == "5":
            second_value = driver.find_elements("xpath", five_2)
            for val_second in second_value:
                val_second.click()
        if a[1] == "6":
            second_value = driver.find_elements("xpath", six_2)
            for val_second in second_value:
                val_second.click()
        if a[1] == "7":
            second_value = driver.find_elements("xpath", seven_2)
            for val_second in second_value:
                val_second.click()
        if a[1] == "8":
            second_value = driver.find_elements("xpath", eight_2)
            for val_second in second_value:
                val_second.click()
        if a[1] == "9":
            second_value = driver.find_elements("xpath", nine_2)
            for val_second in second_value:
                val_second.click()
        if a[2] == "0":
            third_value = driver.find_elements("xpath", zero_3)
            for val_third in third_value:
                val_third.click()
        if a[2] == "1":
            third_value = driver.find_elements("xpath", one_3)
            for val_third in third_value:
                val_third.click()
        if a[2] == "2":
            third_value = driver.find_elements("xpath", two_3)
            for val_third in third_value:
                val_third.click()
        if a[2] == "3":
            third_value = driver.find_elements("xpath", three_3)
            for val_third in third_value:
                val_third.click()
        if a[2] == "4":
            third_value = driver.find_elements("xpath", four_3)
            for val_third in third_value:
                val_third.click()
        if a[2] == "5":
            third_value = driver.find_elements("xpath", five_3)
            for val_third in third_value:
                val_third.click()
        if a[2] == "6":
            third_value = driver.find_elements("xpath", six_3)
            for val_third in third_value:
                val_third.click()
        if a[2] == "7":
            third_value = driver.find_elements("xpath", seven_3)
            for val_third in third_value:
                val_third.click()
        if a[2] == "8":
            third_value = driver.find_elements("xpath", eight_3)
            for val_third in third_value:
                val_third.click()
        if a[2] == "9":
            third_value = driver.find_elements("xpath", nine_3)
            for val_third in third_value:
                val_third.click()
        else:
            print("something happened")
        print(a)

        submit = driver.find_elements("xpath", "//*[@id='root']/div/div[2]/div[3]/button")
        for submitting in submit:
            submitting.click()

if second_question == "n":
    print("aight, so no 251 to 500, dope, buh its logical though")

third_question = input("Should I do third? y/n")
if third_question == "y":
    for a in third_quarter:
        if a[0] == "0":
            first_value = driver.find_elements("xpath", zero_1)
            for val_first in first_value:
                val_first.click()
        if a[0] == "1":
            first_value = driver.find_elements("xpath", one_1)
            for val_first in first_value:
                val_first.click()
        if a[0] == "2":
            first_value = driver.find_elements("xpath", two_1)
            for val_first in first_value:
                val_first.click()
        if a[0] == "3":
            first_value = driver.find_elements("xpath", three_1)
            for val_first in first_value:
                val_first.click()
        if a[0] == "4":
            first_value = driver.find_elements("xpath", four_1)
            for val_first in first_value:
                val_first.click()
        if a[0] == "5":
            first_value = driver.find_elements("xpath", five_1)
            for val_first in first_value:
                val_first.click()
        if a[0] == "6":
            first_value = driver.find_elements("xpath", six_1)
            for val_first in first_value:
                val_first.click()
        if a[0] == "7":
            first_value = driver.find_elements("xpath", seven_1)
            for val_first in first_value:
                val_first.click()
        if a[0] == "8":
            first_value = driver.find_elements("xpath", eight_1)
            for val_first in first_value:
                val_first.click()
        if a[0] == "9":
            first_value = driver.find_elements("xpath", nine_1)
            for val_first in first_value:
                val_first.click()
        if a[1] == "0":
            second_value = driver.find_elements("xpath", zero_2)
            for val_second in second_value:
                val_second.click()
        if a[1] == "1":
            second_value = driver.find_elements("xpath", one_2)
            for val_second in second_value:
                val_second.click()
        if a[1] == "2":
            second_value = driver.find_elements("xpath", two_2)
            for val_second in second_value:
                val_second.click()
        if a[1] == "3":
            second_value = driver.find_elements("xpath", three_2)
            for val_second in second_value:
                val_second.click()
        if a[1] == "4":
            second_value = driver.find_elements("xpath", four_2)
            for val_second in second_value:
                val_second.click()
        if a[1] == "5":
            second_value = driver.find_elements("xpath", five_2)
            for val_second in second_value:
                val_second.click()
        if a[1] == "6":
            second_value = driver.find_elements("xpath", six_2)
            for val_second in second_value:
                val_second.click()
        if a[1] == "7":
            second_value = driver.find_elements("xpath", seven_2)
            for val_second in second_value:
                val_second.click()
        if a[1] == "8":
            second_value = driver.find_elements("xpath", eight_2)
            for val_second in second_value:
                val_second.click()
        if a[1] == "9":
            second_value = driver.find_elements("xpath", nine_2)
            for val_second in second_value:
                val_second.click()
        if a[2] == "0":
            third_value = driver.find_elements("xpath", zero_3)
            for val_third in third_value:
                val_third.click()
        if a[2] == "1":
            third_value = driver.find_elements("xpath", one_3)
            for val_third in third_value:
                val_third.click()
        if a[2] == "2":
            third_value = driver.find_elements("xpath", two_3)
            for val_third in third_value:
                val_third.click()
        if a[2] == "3":
            third_value = driver.find_elements("xpath", three_3)
            for val_third in third_value:
                val_third.click()
        if a[2] == "4":
            third_value = driver.find_elements("xpath", four_3)
            for val_third in third_value:
                val_third.click()
        if a[2] == "5":
            third_value = driver.find_elements("xpath", five_3)
            for val_third in third_value:
                val_third.click()
        if a[2] == "6":
            third_value = driver.find_elements("xpath", six_3)
            for val_third in third_value:
                val_third.click()
        if a[2] == "7":
            third_value = driver.find_elements("xpath", seven_3)
            for val_third in third_value:
                val_third.click()
        if a[2] == "8":
            third_value = driver.find_elements("xpath", eight_3)
            for val_third in third_value:
                val_third.click()
        if a[2] == "9":
            third_value = driver.find_elements("xpath", nine_3)
            for val_third in third_value:
                val_third.click()
        else:
            print("something happened")
        print(a)

        submit = driver.find_elements("xpath", "//*[@id='root']/div/div[2]/div[3]/button")
        for submitting in submit:
            submitting.click()

if third_question == "n":
    print("cool, so no 501 to 750, ok na, buh its logical though")

fourth_question = input("Should I do fourth? y/n")
if fourth_question == "y":
    for a in fourth_quarter:
        if a[0] == "0":
            first_value = driver.find_elements("xpath", zero_1)
            for val_first in first_value:
                val_first.click()
        if a[0] == "1":
            first_value = driver.find_elements("xpath", one_1)
            for val_first in first_value:
                val_first.click()
        if a[0] == "2":
            first_value = driver.find_elements("xpath", two_1)
            for val_first in first_value:
                val_first.click()
        if a[0] == "3":
            first_value = driver.find_elements("xpath", three_1)
            for val_first in first_value:
                val_first.click()
        if a[0] == "4":
            first_value = driver.find_elements("xpath", four_1)
            for val_first in first_value:
                val_first.click()
        if a[0] == "5":
            first_value = driver.find_elements("xpath", five_1)
            for val_first in first_value:
                val_first.click()
        if a[0] == "6":
            first_value = driver.find_elements("xpath", six_1)
            for val_first in first_value:
                val_first.click()
        if a[0] == "7":
            first_value = driver.find_elements("xpath", seven_1)
            for val_first in first_value:
                val_first.click()
        if a[0] == "8":
            first_value = driver.find_elements("xpath", eight_1)
            for val_first in first_value:
                val_first.click()
        if a[0] == "9":
            first_value = driver.find_elements("xpath", nine_1)
            for val_first in first_value:
                val_first.click()
        if a[1] == "0":
            second_value = driver.find_elements("xpath", zero_2)
            for val_second in second_value:
                val_second.click()
        if a[1] == "1":
            second_value = driver.find_elements("xpath", one_2)
            for val_second in second_value:
                val_second.click()
        if a[1] == "2":
            second_value = driver.find_elements("xpath", two_2)
            for val_second in second_value:
                val_second.click()
        if a[1] == "3":
            second_value = driver.find_elements("xpath", three_2)
            for val_second in second_value:
                val_second.click()
        if a[1] == "4":
            second_value = driver.find_elements("xpath", four_2)
            for val_second in second_value:
                val_second.click()
        if a[1] == "5":
            second_value = driver.find_elements("xpath", five_2)
            for val_second in second_value:
                val_second.click()
        if a[1] == "6":
            second_value = driver.find_elements("xpath", six_2)
            for val_second in second_value:
                val_second.click()
        if a[1] == "7":
            second_value = driver.find_elements("xpath", seven_2)
            for val_second in second_value:
                val_second.click()
        if a[1] == "8":
            second_value = driver.find_elements("xpath", eight_2)
            for val_second in second_value:
                val_second.click()
        if a[1] == "9":
            second_value = driver.find_elements("xpath", nine_2)
            for val_second in second_value:
                val_second.click()
        if a[2] == "0":
            third_value = driver.find_elements("xpath", zero_3)
            for val_third in third_value:
                val_third.click()
        if a[2] == "1":
            third_value = driver.find_elements("xpath", one_3)
            for val_third in third_value:
                val_third.click()
        if a[2] == "2":
            third_value = driver.find_elements("xpath", two_3)
            for val_third in third_value:
                val_third.click()
        if a[2] == "3":
            third_value = driver.find_elements("xpath", three_3)
            for val_third in third_value:
                val_third.click()
        if a[2] == "4":
            third_value = driver.find_elements("xpath", four_3)
            for val_third in third_value:
                val_third.click()
        if a[2] == "5":
            third_value = driver.find_elements("xpath", five_3)
            for val_third in third_value:
                val_third.click()
        if a[2] == "6":
            third_value = driver.find_elements("xpath", six_3)
            for val_third in third_value:
                val_third.click()
        if a[2] == "7":
            third_value = driver.find_elements("xpath", seven_3)
            for val_third in third_value:
                val_third.click()
        if a[2] == "8":
            third_value = driver.find_elements("xpath", eight_3)
            for val_third in third_value:
                val_third.click()
        if a[2] == "9":
            third_value = driver.find_elements("xpath", nine_3)
            for val_third in third_value:
                val_third.click()
        else:
            print("something happened")
        print(a)

        submit = driver.find_elements("xpath", "//*[@id='root']/div/div[2]/div[3]/button")
        for submitting in submit:
            submitting.click()

if fourth_question == "n":
    print("aight, no 751 to 999, I believe you shaa, these ones no dey guide well, buh its logical though")

print("done")
