import logging

def configurer_logging():
    logging.basicConfig(filename = 'resultat.txt',level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
