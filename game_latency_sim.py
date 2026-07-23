import time
import random

class NetworkSimulator:
    def __init__(self, base_latency=0.1, jitter=0.05):
        # Base latency in seconds (e.g., 100ms)
        self.base_latency = base_latency
        # Jitter adds random variation to latency
        self.jitter = jitter

    def send_packet(self, data):
        # Simulate network travel time
        simulated_delay = self.base_latency + random.uniform(-self.jitter, self.jitter)
        # Ensure delay is not negative
        simulated_delay = max(0, simulated_delay)
        
        # In a real game, this would involve sending data over a socket.
        # Here, we just simulate the delay.
        time.sleep(simulated_delay)
        
        # In a real scenario, you'd receive a response or confirmation.
        # For this simulation, we just acknowledge the 'transmission'.
        return f"Packet '{data}' received after {simulated_delay:.3f}s delay"

class GameClient:
    def __init__(self, network_simulator):
        self.network = network_simulator

    def send_command(self, command):
        print(f"Sending command: '{command}'...")
        # Simulate sending a game command (e.g., 'move unit A to X,Y')
        response = self.network.send_packet(command)
        print(response)

if __name__ == "__main__":
    # Initialize the network simulator with some latency and jitter
    # This mimics the network conditions described in the article.
    network_sim = NetworkSimulator(base_latency=0.2, jitter=0.1) # 200ms base latency, up to 100ms jitter
    
    # Initialize the game client that uses the simulator
    client = GameClient(network_sim)
    
    print("--- Simulating Game Commands with Network Latency ---")
    
    # Simulate sending a few game commands
    client.send_command("Build Barracks")
    client.send_command("Move Scout Unit 1")
    client.send_command("Attack Enemy Base")
    
    print("--- Simulation Complete ---")
