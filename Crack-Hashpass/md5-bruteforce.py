#usr/bin/python2.7
import time
import itertools, string
import hashlib
import sys
import signal
import threading

info = """
\33[32;1m\
  Name            : crack hash md5 bruteforce
  Created By      : Sefa Said Deniz
  re-author       : cenel kita
  Yutub           : https://youtube.com/c/CenelKITA45
  Documentation   : https://github.com/CenelKITA22/hashpass
  License         : Completely Free
  Thanks to       : Agus Makmun (Summon Agus)-bloggersmart.net - python.web.id
"""
done = False
def signal_handler(signal, frame):
    print 'You pressed Ctrl+C!'
    global done
    done=True
    sys.exit(0)
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done==True:
            break
            
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    


def _attack(chrs, inputt):
    print "[+] Start Time: ", time.strftime('%H:%M:%S')
    start_time = time.time()
    t = threading.Thread(target=animate)
    t.start()
    total_pass_try=0
    for n in range(1, 31+1):
      characterstart_time = time.time()
      print "\n[!] I'm at ", n , "-character"
      
      
      for xs in itertools.product(chrs, repeat=n):

          saved = ''.join(xs)
          stringg = saved
          m = hashlib.md5()
          m.update(saved)
          total_pass_try +=1
          if m.hexdigest() == inputt:
              time.sleep(10)
              global done
              done = True

              print "\33[0;36m [!] Hasilnya: ", stringg
              print "\n[-] End Time: ", time.strftime('%H:%M:%S')
              print "\n[-] Total Keyword attempted: ", total_pass_try
              print("\n---Md5 cracked at %s seconds ---" % (time.time() - start_time))
              sys.exit("Thank You !")

        
      print "\n[!]",n,"-character finished in %s seconds ---" % (time.time() - characterstart_time)
   


def main():
    print info
    
    inp_usr = raw_input(" Masukan code hashnya bro :\n")
    chrs = string.printable.replace(' \t\n\r\x0b\x0c', '')
    print chrs
    signal.signal(signal.SIGINT, signal_handler)
    return _attack( chrs,inp_usr );

   

if __name__ == "__main__":
    main()
   
   
   
