from manager import MurderStatsManager  # Importi klass manager2-st


manager = MurderStatsManager()
manager.add_data('Europe', 'Estonia', 'Tallinn', 5)
manager.add_data('Europe', 'Finland', 'Helsinki', 3)
manager.add_data('Asia', 'Japan', 'Tokyo', 8)
print(manager.get_stats())


              
              
          
