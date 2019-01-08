# -*- coding: utf-8 -*-

# FAO Translators:
# First of all thank you for your interest in translating this game,
# I will be grateful if you could share it with the community -
# if possible please send it back to my email, and I'll add it to the next version.

# The translation does not have to be exact as long as it makes sense and fits in its location
# (if it doesn't I'll try to either make the font smaller or make the area wider - where possible).
# The colour names in other languages than English are already in smaller font.

d = dict()
dp = dict()  # messages with pronunciation exceptions - this dictionary will override entries in a copy of d

d["local_kbrd"] = "Ελληνικά γράμματα"
numbers = ['ένα', 'δύο', 'τρία', 'τέσσερα', 'πέντε', 'έξι', 'επτά', 'οκτώ', 'εννέα', 'δέκα', 'έντεκα', 'δώδεκα',
           'δεκατρία', 'δεκατέσσερα', 'δεκαπέντε', 'δεκαέξι', 'δεκαεπτά', 'δεκαοκτώ', 'δεκαεννέα', 'είκοσι',
           'είκοσι ένα', 'είκοσι δύο', 'είκοσι τρία', 'είκοσι τέσσερα', 'είκοσι πέντε', 'είκοσι έξι', 'είκοσι επτά',
           'είκοσι οκτώ', 'είκοσι εννέα']
numbers2090 = ['είκοσι', 'τριάντα', 'σαράντα', 'πενήντα', 'εξήντα', 'εβδομήντα', 'ογδόντα', 'ενενήντα']

dp['abc_flashcards_word_sequence'] = ['Άλογο', 'Βάρκα', 'Γάτα', 'Δέντρο', 'Ελέφαντας', 'Ζέβρα', 'Ήλιος', 'Θάμνος',
                                      'Ιπποπόταμος', 'Καμηλοπάρδαλη', 'Λουλούδια', 'Μήλο', 'Ντομάτα', 'Ξυλόφωνο',
                                      'Ομπρέλα', 'Πάπια', 'Ρούχα', 'Σπίτι', 'Τσαγιέρα', 'Ύπνος', 'Φορτηγό', 'Χιμπατζής',
                                      'Ψάρι', 'Ώρα']
d['abc_flashcards_word_sequence'] = ['<1>Ά<2>λογο', '<1>Β<2>άρκα', '<1>Γ<2>άτα', '<1>Δ<2>έντρο',
                                     '<1>Ε<2>λ<1>έ<2>φαντας', '<1>Ζ<2>έβρα', '<1>Ή<2>λιος', '<1>Θ<2>άμνος',
                                     '<1>Ι<2>πποπόταμος', '<1>Κ<2>αμηλοπάρδαλη', '<1>Λ<2>ου<1>λ<2>ούδια', '<1>Μ<2>ήλο',
                                     '<1>Ν<2>τομάτα', '<1>Ξ<2>υλόφωνο', '<1>Ο<2>μπρέλα', '<1>Π<2>ά<1>π<2>ια',
                                     '<1>Ρ<2>ούχα', '<1>Σ<2>πίτι', '<1>Τ<2>σαγιέρα', '<1>Ύ<2>πνος', '<1>Φ<2>ορτηγό',
                                     '<1>Χ<2>ιμπατζής', '<1>Ψ<2>άρι', '<1>Ώ<2>ρα']

d['abc_flashcards_frame_sequence'] = [45, 1, 2, 31, 4, 25, 18, 46, 47, 30, 36, 42, 33, 23, 20, 3, 48, 7, 19, 49, 50, 37,
                                      5, 51]

# alphabet gr
alphabet_lc = ['α', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'θ', 'ι', 'κ', 'λ', 'μ', 'ν', 'ξ', 'ο', 'π', 'ρ', 'σ', 'τ', 'υ', 'φ',
               'χ', 'ψ', 'ω']
alphabet_uc = ['Α', 'Β', 'Γ', 'Δ', 'Ε', 'Ζ', 'Η', 'Θ', 'Ι', 'Κ', 'Λ', 'Μ', 'Ν', 'Ξ', 'Ο', 'Π', 'Ρ', 'Σ', 'Τ', 'Υ', 'Φ',
               'Χ', 'Ψ', 'Ω']
# correction of eSpeak pronounciation of single letters if needed
letter_names = []

accents_lc = ['-', 'ς', 'ά', 'έ', 'ή', 'ί', 'ϊ', 'ό', 'ύ', 'ώ']
accents_uc = ['Ά', 'Έ', 'Ή', 'Ί', 'Ϊ', 'Ό', 'Ύ', 'Ώ']


def n2txt(n, twoliner=False):
    "takes a number from 1 - 99 and returns it back in a word form, ie: 63 returns 'sixty three'."
    if 0 < n < 30:
        return numbers[n - 1]
    elif 30 <= n < 100:
        m = n % 10
        tens = numbers2090[(n // 10) - 2]
        if m == 0:
            return tens
        elif m > 0:
            ones = numbers[m - 1]
            if twoliner:
                return [tens, ones]
            else:
                return tens + " " + ones

    elif n == 0:
        return "μηδέν"
    elif n == 100:
        return "εκατό"
    return ""


hrs = ['μία', 'δύο', 'τρεις', 'τέσσερις', 'πέντε', 'έξι', 'επτά', 'οκτώ', 'εννέα', 'δέκα', 'έντεκα', 'δώδεκα']


def time2str(h, m):
    'takes 2 variables: h - hour, m - minute, returns time as a string, ie. five to seven - for 6:55'
    if m > 30:
        if h == 12:
            h = 1
        else:
            h += 1
    if m == 0:
        return "%s ακριβώς" % hrs[h - 1]
    elif m == 1:
        return "%s και ένα λεπτό" % hrs[h - 1]
    elif m == 15:
        return "%s και τέταρτο" % hrs[h - 1]
    elif m == 30:
        return "%s και μισή" % hrs[h - 1]
    elif m == 45:
        return "%s παρά τέταρτο" % hrs[h - 1]
    elif m == 59:
        return "%s παρά ένα λεπτό" % hrs[h - 1]
    elif m < 30:
        return "%s και %s" % (hrs[h - 1], n2txt(m))
    elif m > 30:
        return "%s παρά %s" % (hrs[h - 1], n2txt(60 - m))
    return ""

#write a fraction in words
numerators = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
d_singular = ['', 'half', 'third', 'quarter', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']
d_plural = ['', 'halves', 'thirds', 'quarters', 'fifths', 'sixths', 'sevenths', 'eighths', 'ninths', 'tenths', 'elevenths', 'twelfths']

def fract2str(n, d):
    if n == 1:
        return numerators[0] + " " + d_singular[d-1]
    else:
        return numerators[n-1] + " " + d_plural[d-1]

d["a4a_animals"] = ["αγελάδα", "γαλοπούλα", "γαρίδα", "λύκος", "πάνθηρας", "πάντα", "καρακάξα", "στρείδι", "πόνυ",
                    "ποντίκι", "παγκ", "κοάλα", "βάτραχος", "πασχαλίτσα", "γορίλας", "λάμα", "όρνιο", "χάμστερ",
                    "πουλί", "αστερίας", "κοράκι", "παπαγάλος", "κάμπια", "τίγρης", "κολίμπρι", "πιράνχα", "γουρούνι",
                    "σκορπιός", "αλεπού", "λεοπάρδαλη", "ιγκουάνα", "δελφίνι", "νυχτερίδα", "νεοσσός", "καβούρι",
                    "κότα", "σφήκα", "χαμαιλέοντας", "φάλαινα", "σκαντζόχοιρος", "ελαφάκι", "τάρανδος", "μέλισσα",
                    "οχιά", "κεφαλάς", "γάιδαρος", "ινδικό χοιρίδιο", "βραδύποδας", "άλογο", "πιγκουίνος", "βίδρα",
                    "αρκούδα", "ζέβρα", "στρουθοκάμηλος", "καμήλα", "αντιλόπη", "λεμούριος", "περιστέρι", "λάμα",
                    "τυφλοπόντικας", "σαλάχι", "κριάρι", "κουνάβι", "μέδουσα", "πρόβατο", "καρχαρίας", "γατάκι",
                    "ελάφι", "σαλιγκάρι", "φλαμίνγκο", "κουνέλι", "μύδι", "κάστορας", "σπουργίτι", "περιστέρι", "αετός",
                    "σκαθάρι", "ιπποπόταμος", "κουκουβάγια", "κόμπρα", "σαλαμάνδρα", "χήνα", "κανγκουρό", "λιβελούλα",
                    "φρύνος", "πελεκάνος", "καλαμάρι", "λιονταράκι", "τζάγκουαρ", "πάπια", "σαύρα", "ρινόκερος",
                    "ύαινα", "βόδι", "παγώνι", "παπαγάλος", "ελάφι", "αλιγάτορας", "μυρμήγκι", "γίδα", "κουνελάκι",
                    "λιοντάρι", "σκίουρος", "οπόσσουμ", "χιμπατζής", "ελαφίνα", "σκίουρος", "ελέφαντας",
                    "καμηλοπάρδαλη", "αράχνη", "σκυλάκι", "κίσσα", "φώκια", "πετεινός", "χελώνα", "ταύρος", "γάτα",
                    "αρουραίος", "γυμνοσάλιαγκας", "βουβάλι", "κότσυφας", "κύκνος", "αστακός", "σκύλος",
                    "κουνούπι", "φίδι", "κοτόπουλο", "μυρμηγκοφάγος"]
d["a4a_sport"] = ["τζούντο", "πισίνα", "ποδηλατάδα", "εκτάσεις", "κράνος", "πατινάζ", "περπάτημα", "τρέξιμο",
                  "κολύμπι", "τραμπολίνο", "περίπατος", "μποξ", "χόκεϋ", "αγώνας", "ρίψη", "πατίνι", "νίκη", "κάθισμα",
                  "σκι", "γκολ", "σφυρίχτρα", "δάδα", "ιστιοπλοΐα", "έκταση", "τένις", "αναπήδηση", "κωπηλασία",
                  "τρέξιμο", "σχοινάκι"]
d["a4a_body"] = ["δόντια", "μάγουλα", "αστράγαλος", "γόνατο", "δάκτυλο", "μυς", "στόμα", "πόδια", "χέρι", "αγκώνας",
                 "μαλλιά", "βλεφαρίδα", "γένια", "αφαλός", "αντίχειρας", "στήθος", "ρουθούνι", "μύτη", "ισχίο", "χέρι",
                 "φρύδι", "γροθιά", "λαιμός", "καρπός", "λαιμός", "μάτι", "πόδι", "σπονδυλική στήλη", "αυτί", "δάκτυλο",
                 "πόδι", "κοτσίδα", "πρόσωπο", "πλάτη", "πηγούνι", "πισινός", "μηρός", "κοιλιά"]
d["a4a_people"] = ["κορίτσι", "αρσενικό", "γιός", "κολλητοί", "φίλοι", "μωρό", "παιδί", "μπαμπάς", "μαμά",
                   "δίδυμα αγόρια", "αδέρφια", "άντρας", "μαμά", "παππούς", "οικογένεια", "θηλυκό", "η σύζυγος",
                   "ο σύζυγος", "νύφη", "κυρία", "γιαγιά", "ζευγάρι", "τύπος", "δίδυμα κορίτσια", "φυλή", "αγόρι",
                   "αδερφές", "γυναίκα", "κυρία"]
d["a4a_food"] = ["καραμέλα", "λουκάνικο", "χάμπουργκερ", "μπριζόλα", "μπισκοτάκι", "λουκουμάς", "καρύδα", "ρύζι",
                 "παγωτό", "ζελέ", "γιαούρτι", "επιδόρπιο", "πρέτζελ", "φυστίκι", "μαρμελάδα", "συμπόσιο", "μπισκότο",
                 "μπέηκον", "καρύκευμα", "καφές", "πίτα", "λεμονάδα", "σοκολάτα", "μπουκάλι νερού", "μεσημεριανό",
                 "πάγος", "ζάχαρη", "σάλτσα", "σούπα", "χυμός", "τηγανιτές πατάτες", "κέηκ", "πουρές", "τσάι", "ψωμάκι",
                 "τυρί", "βοδινό", "σάντουιτς", "κομμάτι", "πασπάλισμα", "πίτσα", "αλεύρι", "τσίχλα", "σπαγγέτι",
                 "ψητό", "βραστό", "αλοιφή", "κρέας", "γάλα", "γεύμα", "καλαμπόκι", "ψωμί", "καρύδι", "αυγό",
                 "χοτ ντογκ", "ζαμπόν"]
d["a4a_clothes_n_accessories"] = ["κοσμήματα", "κάλτσα", "μπουφάν", "τακούνι", "φόρμα", "βερμούδα", "τσέπη",
                                  "μενταγιόν", "αθλητική φόρμα", "στολή", "αδιάβροχο", "παντελόνι", "γυαλιά ηλίου",
                                  "παλτό", "πουλόβερ", "πουκάμισο", "σανδάλια", "κουστούμι", "πυτζάμες", "φούστα",
                                  "φερμουάρ", "παπούτσια", "κόσμημα", "γραβάτα", "παντόφλες", "γάντια", "καπέλο",
                                  "μανίκι", "καπέλο", "μαγιό", "φόρμα", "γιλέκο", "γυαλιά", "κορδόνι", "μπάλωμα",
                                  "κασκόλ", "παπούτσι", "κουμπί", "φόρεμα", "ζώνη", "σόλα", "ρόμπα", "εσώρουχα",
                                  "κιμονό", "φόρμα"]
d["a4a_actions"] = ["γλύφω", "καρφώνω", "παρακαλώ", "πέφτω", "γρατζουνώ", "αγγίζω", "μυρίζω", "βλέπω", "σκαρφαλώνω",
                    "σκάβω", "ουρλιάζω", "κοιμάμαι", "εξερευνώ", "ζωγραφίζω", "αγκαλιάζω", "διδάσκω", "ύπνος", "πηλός",
                    "πιάνω", "χειροκροτώ", "κλαίω", "τραγουδώ", "συναντώ", "πουλάω", "τσιμπώ", "χτυπώ", "γονατίζω",
                    "βρίσκω", "χορεύω", "βήχω", "κόβω", "σκέφτομαι", "γαβγίζω", "μιλώ", "επευφημώ", "ψήνω", "γράφω",
                    "γρονθοκοπώ", "γρατζουνώ", "μελετώ", "οργώνω", "ονειρεύομαι", "ταχυδρομώ", "βουτώ", "ψιθυρίζω",
                    "σιγοκλαίω", "κουνώ", "ταίζω", "σέρνομαι", "κατασκηνώνω", "ρίχνω", "καθαρίζω", "φωνάζω", "κλαίω",
                    "επιπλέω", "τραβώ", "τρώω", "φιλώ", "κάθομαι", "εκκολάπτω", "βλεφαρίζω", "ακούω", "φιλώ", "παίζω",
                    "πλένω", "συζητώ", "οδηγώ", "πίνω", "πετώ", "ταχυδακτυλουργώ", "δαγκώνω", "σκουπίζω", "βλέπω",
                    "πλέκω", "σηκώνω", "φέρνω", "διαβάζω", "κρώζω", "κοιτώ επίμονα", "τρώω"]
d["a4a_construction"] = ["φάρος", "πόρτα", "τσίρκο", "εκκλησία", "κυνοτροφείο", "ναός", "καπνός", "καμινάδα", "τούβλο",
                         "πηγάδι", "δρόμος", "κάστρο", "κατάστημα", "σκάλα", "σχολείο", "φάρμα", "γέφυρα", "φράγμα",
                         "πυραμίδα", "αχυρώνας", "μύλος", "παράθυρο", "καλύβα", "σκαλί", "μαγαζί", "παράγκα", "στέγη",
                         "καμπαναριό", "γκαράζ", "τζαμί", "νοσοκομείο", "σκηνή", "σπίτι", "τοίχος", "τράπεζα",
                         "παντζούρια", "καλύβα"]
d["a4a_nature"] = ["γη", "γκρεμός", "λόφος", "φαράγγι", "βράχος", "θάλασσα", "λίμνη", "όχθη", "ακτή", "βουνό",
                   "λιμνούλα", "κορυφή", "λάβα", "σπηλιά", "αμμόλοφος", "νησί", "δάσος", "έρημος", "παγόβουνο"]
d["a4a_jobs"] = ["κλόουν", "μηχανικός", "ιερέας", "κτηνίατρος", "δικαστής", "μάγειρας", "αθλητής", "βιβλιοθηκάριος",
                 "ζογκλέρ", "αστυνόμος", "υδραυλικός", "σήμα", "βασίλισσα", "αγρότης", "μάγος", "ιππότης", "γιατρός",
                 "χτίστης", "καθαριστής", "δασκάλα", "κυνητός", "στρατιώτης", "μουσικός", "δικηγόρος", "ψαράς",
                 "πριγκήπισσα", "πυροσβέστης", "καλόγρια", "πειρατής", "αγελαδάρης", "ηλεκτρολόγος",
                 "νοσοκόμα", "βασιλιάς", "πρόεδρος", "γραφείο", "ξυλουργός", "καβαλάρης", "εργάτης", "μηχανικός",
                 "πιλότος", "ηθοποιός", "μάγειρας", "μαθητής", "χασάπης", "λογιστής", "πρίγκηπας", "ιερέας", "ναύτης",
                 "μποξέρ", "μπαλαρίνα", "προπονητής", "αστροναύτης", "ζωγράφος", "αναισθησιολόγος", "επιστήμονας"]
d["a4a_fruit_n_veg"] = ["καρότο", "μαύρα μούρα", "σέλινο", "γογγύλι", "κακάο", "ροδάκινο", "πεπόνι", "γκρέιπφρουτ",
                        "μπρόκολο", "σταφύλια", "σπανάκι", "σύκο", "κουκούτσι", "ραπανάκι", "ντομάτα", "ακτινίδιο",
                        "σπαράγγι", "ελιές", "αγγούρια", "φασόλια", "φράουλα", "πιπεριές", "μούρο", "βερύκοκκο",
                        "πατάτες", "μπιζέλια", "λάχανο", "κεράσια", "κολοκύθα", "μπλε μούρα", "αχλάδι", "πορτοκάλι",
                        "κολοκύθι", "αβοκάντο", "σκόρδο", "κρεμμύδι", "μήλο", "λάιμ", "κουνουπίδι", "μάνγκο", "μαρούλι",
                        "λεμόνι", "μελιτζάνα", "αγκινάρα", "δαμάσκηνα", "πράσο", "μπανάνες", "παπάγια"]
d["a4a_transport"] = ["πανί", "ταξί", "αυτοκίνητο", "ποδήλατο", "σχεδία", "πηδάλι", "λεωφορείο", "τιμόνι", "βάρκα",
                      "φορτηγό", "έλκυθρο", "χαλί", "μοτοσυκλέτα", "τρένο", "πλοίο", "βαν", "κανό", "πύραυλος",
                      "κατάρτι", "έλκυθρο", "ποδήλατο"]
