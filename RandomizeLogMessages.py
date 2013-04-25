import sublime, sublime_plugin, random, re, os, math

class RandomizeLogMessages(sublime_plugin.EventListener):
    def on_pre_save(self, view):

        RANDOM_NUMBER_LENGTH = 7

        FILE_EXTENSIONS = [".js"]

        #Only for the listed extensions
        filename, extension = os.path.splitext(view.file_name())
        if extension in FILE_EXTENSIONS:

            edit = view.begin_edit()

            #Get regions with log messages
            regions = view.find_all(r"log\('.*'?\);?")
            regions.reverse()

            for region in regions:

                text = view.substr(region)

                #If this doesn't contain a log reference already,
                if not re.search(r"\(\d{" + str(RANDOM_NUMBER_LENGTH) + "}\)", text):

                    lbound = math.pow(10, RANDOM_NUMBER_LENGTH - 1)
                    ubound = 10 * lbound - 1

                    ref = " (" + str(random.randrange(lbound, ubound)) + ")"

                    text = re.sub(r"(log\(.+)(')", r"\1" + ref + r"\2", text)

                    #Update this log message
                    view.replace(edit, region, text)


            view.end_edit(edit)
   

