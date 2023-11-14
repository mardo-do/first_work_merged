




def function_json_to_csv(path_to_json, path_to_csv):
   the_csv = open(path_to_csv+"/file.csv", "w")
   datas = ""
   buff = open("buffer_file.txt", "w")

   with open(path_to_json, "r") as f:
      for line in f:
         buff.write(line)

   buff.close()
   
# let's make use of another file with extension : txt, just cause, there's too much constraints in 
# using directly the json file

   buff_read = open("buffer_file.txt", "r")

   for line in buff_read:
      datas += str(line)

   buff_read.close()
   

   variable_guide = ""
   ind = 0

   # removing all free-spaces
   data_normal = datas
   data_without_space = datas = datas.replace(" ", "")
   data_without_double = datas = datas.replace('"', '')

   var_lengh = len(datas)

   my_list_data = []

   for x in range(0,var_lengh):
      
      if datas[x] == ":":
      # getting keys...
         variable_left = ""
         var_left = ""
         y = x - 1
         while ((datas[y] != ",") and (datas[y] != "{")):
            variable_left += datas[y]
         
            y -= 1

         for v in range(0, len(variable_left)):
            var_left += variable_left[len(variable_left) - (v+1)]
      
         my_list_data.append(str(var_left))






   # Getting all index...
   all_index = []
   for each in my_list_data:
      each = str(each)
      each = each.replace("\n", "")
      each_in_string = '"'+each+'"'
      all_index.append(data_normal.find(str(each_in_string)))





   each_block_right = ""
   for each in my_list_data:
      each = str(each)
      each = each.replace("\n", "")
      each_in_string = '"'+each+'"'
      if(each_in_string in each_block_right):
         continue
      #print(each_in_string)
      #print(data_normal.find(str(each_in_string)))
      #print(len(each_in_string))
      after_what = data_normal.find(each_in_string) + len(each_in_string)

      #print(after_what)

      #if a key is 
      # if(each in each_block_right):
      #    continue

      test = True
      value_created = ""
      val = 1
   
      while test:
     
         end = True
         while end:
            after_what += 1
            if after_what in all_index:
               end = False
            elif after_what == len(data_normal):
               end = False
            else: 
               value_created += data_normal[after_what]
         
                  
            
         final_value = ""
         for ea in range(0, len(value_created)):
            if value_created[ea] == ",":
               # value_created.replace(value_created[ea], "_", -1)
               final_value += "_"
            else:
               final_value += value_created[ea]

         print(each_in_string+" , "+final_value)
         the_csv.write(each_in_string+" , "+final_value+ "\n")
         each_block_right += value_created

         test = False   






   f.close()
   the_csv.close()








# second function

def function_first(path_json, path_csv):
   datas = ""
   buff = open("buffer_file.txt", "w")

   if path_json.endswith(".json"):
      # test_constraint = 0
      # if datas.startswith("{") and datas.endswith("}"):
      #    test_constraint += 1
      # else:
      #    test_constraint -= 1

      # if (datas.find("None") > 0 or datas.find("True") > 0 or datas.find("False") > 0):
      #    test_constraint -= 1

      # if test_constraint > 1:
      function_json_to_csv(path_json, path_csv)
      # else:
      #    print("Problem with datas... ")
   else:
      print("Problem file extension...")










# calling of the function
function_first("file2.json", "/home/negre/negre_python/nuls/Tp")












