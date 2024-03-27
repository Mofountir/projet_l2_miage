import binascii
import struct # pour unpack
import syntaxe

def analyse_semantique(trame):
    """
    Analyse une trame Ethernet :  cf https://fr.wikipedia.org/wiki/Ethernet    
    Input : trame est un tableau d'octets
    """
    print("-"*60)
    print ("\nTrame Ethernet en cours d'analyse ({}): \n{} ... ".format( type(trame), trame[0:10]))
  
    # Analyse du header ETHERNET
    eth_header = trame[0:14]
    #print(eth_header)

    # Analyse de la Data/Charge
    eth_data  = trame[14:34]
    #print(trame[14:34].hex(':'))

    # https://docs.python.org/fr/3/library/struct.html
    eth_mac_dest, eth_mac_src, eth_type = struct.unpack('!6s6sH' , eth_header)
    

    print ('Destination MAC : {}'.format(eth_mac_dest.hex(":"))) # .hex() ssi Python > 3.8
    print ('Source MAC \t: {}'.format(binascii.hexlify(eth_mac_src))) # on refait une chaine du tab de byte.
    print ('EtherType \t: {}'.format(eth_type))
    #https://fr.wikipedia.org/wiki/EtherType pour savoir quel etherType


    version, type_de_service, longueur_totale, identification, flags, fragment_offset, temps_de_vie, protocole, header_checksum, adresse_source, adresse_destination = struct.unpack('!BBHBBBBBBH', eth_data)
    print ('Adresse destination: {}'.format(adresse_destination.hex(":"))) # .hex() ssi Python > 3.8
    print ('Adresse Sources\t: {}'.format(binascii.hexlify(adresse_source))) # on refait une chaine du tab de byte.
    print ('EtherType \t: {}'.format(protocole))
    #https://en.wikipedia.org/wiki/List_of_IP_protocol_numbers pour identifier le protocole

    #https://stackoverflow.com/questions/4959741/python-print-mac-address-out-of-6-byte-string

    ##########################################################
    # TODO : Maintenant que vous avez compris il faut analyser la suite de la trame  !!!

#=================================================================
if __name__ == '__main__':
    filename = "XXX.txt"
    # Analyse syntaxique
    lestrames = syntaxe.analyse_syntaxique(filename)
    # Analyse sémantique 
    for trame in lestrames:
        analyse_semantique(trame)        
