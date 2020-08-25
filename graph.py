class Graph:
    frame0 = """
     ______________________________________________________
     |        Good Graph        |	    Bad Graph	  |
     |                          |    			  |
    S|                          |          		  |
    t|                          |          		  |
    o|                          |           	  	  |
    n|                          |          		  |
    k|                          |          		  |
    s|                          |          		  |
     |                          |          		  |
     |                          |          		  |
     |                          |          		  |
     ------------------------------------------------------
	 Time
	"""
	
    frame1 = """
     ______________________________________________________
     |        Good Graph        |	    Bad Graph	  |
     |                          |#    			  |
    S|                          |          		  |
    t|                          |          		  |
    o|                          |           	  	  |
    n|                          |          		  |
    k|                          |          		  |
    s|                          |          		  |
     |                          |          		  |
     |                          |          		  |
     |#                         |          		  |
     ------------------------------------------------------
	 Time
	"""
	
    frame2 = """
     ______________________________________________________
     |        Good Graph        |	    Bad Graph	  |
     |                          |#    			  |
    S|                          | #        		  |
    t|                          |          		  |
    o|                          |           	  	  |
    n|                          |          		  |
    k|                          |          		  |
    s|                          |          		  |
     |                          |          		  |
     | #                        |          		  |
     |#                         |          		  |
     ------------------------------------------------------
	 Time
	"""
	
    frame3 = """
     ______________________________________________________
     |        Good Graph        |	    Bad Graph	  |
     |                          |#    			  |
    S|                          | #        		  |
    t|                          |  #       		  |
    o|                          |           	  	  |
    n|                          |          		  |
    k|                          |          		  |
    s|                          |          		  |
     |  #                       |          		  |
     | #                        |          		  |
     |#                         |          		  |
     ------------------------------------------------------
	 Time
	"""
	
    frame4 = """
     ______________________________________________________
     |        Good Graph        |	    Bad Graph	  |
     |                          |#    			  |
    S|                          | #        		  |
    t|                          |  #       		  |
    o|                          |   #        	  	  |
    n|                          |          		  |
    k|                          |          		  |
    s|   #                      |          		  |
     |  #                       |          		  |
     | #                        |          		  |
     |#                         |          		  |
     ------------------------------------------------------
	 Time
	"""
	
    frame5 = """
     ______________________________________________________
     |        Good Graph        |	    Bad Graph	  |
     |                          |#    			  |
    S|                          | #        		  |
    t|                          |  #       		  |
    o|                          |   #        	  	  |
    n|                          |    #     		  |
    k|    #                     |          		  |
    s|   #                      |          		  |
     |  #                       |          		  |
     | #                        |          		  |
     |#                         |          		  |
     ------------------------------------------------------
	 Time
	"""
	
    frame6 = """
     ______________________________________________________
     |        Good Graph        |	    Bad Graph	  |
     |                          |#    			  |
    S|                          | #        		  |
    t|                          |  #       		  |
    o|                          |   #        	  	  |
    n|     #                    |    #     		  |
    k|    #                     |     #    		  |
    s|   #                      |          		  |
     |  #                       |          		  |
     | #                        |          		  |
     |#                         |          		  |
     ------------------------------------------------------
	 Time
	"""
	
    frame7 = """
     ______________________________________________________
     |        Good Graph        |	    Bad Graph	  |
     |                          |#    			  |
    S|                          | #        		  |
    t|                          |  #       		  |
    o|      #                   |   #        	  	  |
    n|     #                    |    #     		  |
    k|    #                     |     #    		  |
    s|   #                      |      #   		  |
     |  #                       |          		  |
     | #                        |          		  |
     |#                         |          		  |
     ------------------------------------------------------
	 Time
	"""
	
    frame8 = """
     ______________________________________________________
     |        Good Graph        |	    Bad Graph	  |
     |                          |#    			  |
    S|                          | #        		  |
    t|       #                  |  #       		  |
    o|      #                   |   #        	  	  |
    n|     #                    |    #     		  |
    k|    #                     |     #    		  |
    s|   #                      |      #   		  |
     |  #                       |       #  		  |
     | #                        |          		  |
     |#                         |          		  |
     ------------------------------------------------------
	 Time
	"""
	
    frame9 = """
     ______________________________________________________
     |        Good Graph        |	    Bad Graph	  |
     |                          |#    			  |
    S|        #                 | #        		  |
    t|       #                  |  #       		  |
    o|      #                   |   #        	  	  |
    n|     #                    |    #     		  |
    k|    #                     |     #    		  |
    s|   #                      |      #   		  |
     |  #                       |       #  		  |
     | #                        |        # 		  |
     |#                         |          		  |
     ------------------------------------------------------
	 Time
	"""
    
    frame10 = """
     ______________________________________________________
     |        Good Graph        |	    Bad Graph	  |
     |         #                |#    			  |
    S|        #                 | #        		  |
    t|       #                  |  #       		  |
    o|      #                   |   #        	  	  |
    n|     #                    |    #     		  |
    k|    #                     |     #    		  |
    s|   #                      |      #   		  |
     |  #                       |       #  		  |
     | #                        |        # 		  |
     |#                         |         #		  |
     ------------------------------------------------------
	 Time
	"""		
    frame = [frame0, frame1, frame2, frame3, frame4, frame5, frame6, frame7, frame8, frame9, frame10]

    stonks = """                                                                                                    
                                                                                                    
                                                                           ``                       
                                                                         `-/:                       
                                     `..--...`                         `.////`                      
                                  `-/ooooo+///:-`                     .://///:                      
                                 `://++oo+//:////`                  `:////////`                     
                                `:--:/+oo+/+++//:-                `-//////////-                     
                               `:////+oss+/ooo++ss               .:////////////`                    
                               .++oooossso//://+/+`             `..--//////////-                    
                               -ossssssyyso+++/+++`                 .///////-:::`                   
                               `sssyyyyyyso++oyso:                  ://////-                        
                                +syyyhhyyysoosso+`                 .///////`                        
                                .sssyhhhhhyso+/:`                  ://////-                         
                                 /ossyyyhdddo+/`                  .///////`                         
                                -hyossssyyho                      ://////-                          
                          `-+sydmmNdyosssys:/-`                  .///////`                          
                     `:+oyhddmmNmmNNmh//o/-`yddys+:.`            ://////-                           
                    +dmmmmddmmmmmmmmmmd++oo+ydddmmdddyo/.       .///////`                           
                   `hdmmmmmmmmdmmmmmmmmmdyo+ddddmmmmddddd/      ://////-                            
                    odmmmmmmmmmmmNmmdmmmmmy+yddddmmmdmmddy`    .///////`                            
                    :ydmmmmmmmmmmNNNmmmmmmmdymdddmmmmmmdmd+    ://////-                             
                    .yhdmmmmmmmmmmNNmmmmmmmmmmdddmmdmmmmmdd.  .///////`                             
                    `oydmmmmmmmmmNNNNmmmddmmmmdmmmmdmNmmmdds  ://////-                              
                     /hddmmmmmmmdmMNNmmmmmddmmmdmmmddNmmmmmd+.-::////`                              
                     `syhdmmmmmd+oNNNmmmmmmmmmNNmmmdmmNNmmmdds`  ``..                               
                      :yhddmmmmmmdhmmmmmmmmmmmmmNmmdddNNNmmdddy-                                    
                      `syhddmmmmmmmmmdmdddddddddddddo:/sdNmmmmmy`                                   
                       .hhhhdmmmmmmmmmmmmmmmmmmmmmddd/::ommmmmmdo                                   
                        -dhhdmmNmmmmmmmmmmmmmmmmmmddddddmmmmmdmmd-                                  
                        .mdhddmNNNNNmmmmmmmmmmmmmmmmmmmmmmmmmmmmd+                                  
                         yNNNNmmNNNNNNNNNNmmmmmNmmmmmmmmmmmmmmmmmo                                  
                         smNMNNNNMMMmdddhhhmMMNNNNNNNmmmmmmmmmmdo`                                  
                        `ddNNNNMMMMMMMNNmmdmNNNNNNNNNNNNNmoo+/-`                                    
                        `ymmmNNNNNNNMMMNNMMMMNNNNNNNNNNNNN.                                         
                         sdNNNNNNNNNNNNNNMMMMNNNNNmmNNNNmm/                                         
                         omNNNNNNNNNNNNNNNMMMMNNNmyhmmmmmm/                                         
                         /yyyyyyyyyyyyyyyyyyyyyyyyoosyyysy+                                         
                                                                                                    
                                                                                                    
    """
	
	
