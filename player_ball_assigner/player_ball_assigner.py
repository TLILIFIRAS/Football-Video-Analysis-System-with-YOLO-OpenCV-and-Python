import sys 
sys.path.append('../')
from utils import get_center_of_bbox , measure_distance


class PlayerBallAssigner():
    def __init__(self):
        self.max_player_ball_distance = 70 #pexels
        
    def assign_ball_to_player(self,players,ball_box):
        ball_positions = get_center_of_bbox(ball_box)
        minimum_distance = 99999
        assigned_player = -1
        
        for player_id , player in players.items():
            player_bbox=player['bbox']
            distance_left = measure_distance((player_bbox[0],player_bbox[-1]),ball_positions)
            distance_right = measure_distance((player_bbox[2],player_bbox[-1]),ball_positions)
            distance = min(distance_left,distance_right)
            
            if distance < self.max_player_ball_distance :
                if distance < minimum_distance:
                    minimum_distance = distance
                    assigned_player = player_id
        return assigned_player