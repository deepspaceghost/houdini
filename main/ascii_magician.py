class ASCII_Magician():

    def voila(self, butt_key, logger):
        """
        """

        print("Checking number...")
        logger.info("Checking number...")
        if butt_key > 1114111 or butt_key < 0:
            print("What does Solaris want from us?")
            logger.info("What does Solaris want from us?")
            print("{0} is either not within range, or is not an integer.".format(butt_key))
            logger.info("{0} is either not within range, or is not an integer.".format(butt_key))
            print("To continue, try a number between 0 and 1,114,111.")
            logger.info("To continue, try a number between 0 and 1,114,111.")
            return None

        else:
            print("Converting integer...")
            logger.info("Converting integer...")
            chango = chr(butt_key)
            logger.info(chango)
            return chango
