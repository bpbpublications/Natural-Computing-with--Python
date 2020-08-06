#Siperpinski Triangle by Cellular Automata

cells_status = [
      0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
      0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,
      0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

cells_status_appo = cells_status[:]
dic = {0:'-', 1:'*'}
print  (''.join( [dic[e] for e in cells_status_appo]))
step = 1
while(step < 32):
   cells_status_appo = []
   for i in range(0,64):
      if i > 0 and i < 63:
         if cells_status[i-1] == cells_status[i+1]:
            cells_status_appo.append(0)
         else:
            cells_status_appo.append(1)
      elif(i == 0):
         if cells_status[1] == 1:
            cells_status_appo.append(1)
         else:
            cells_status_appo.append(0)
      elif(i == 63):
         if cells_status[62] == 1:
            cells_status_appo.append(1)
         else:
            cells_status_appo.append(0)
   print  (''.join( [dic[e] for e in cells_status_appo]))
   cells_status = cells_status_appo[:]
   step += 1


