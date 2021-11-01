from .models import Player

"""
amount: (int) amount to send
senderMCUsername: (str) mc username of person sending cobble
recieverMCUsername: (str) mc username of person recieving cobble
returns (bool): Returns true on success! false on fail.
"""
def send_cobble(amount, senderPlayer, recieverPlayer):
    if senderPlayer.cobbleCoinHold < amount or senderPlayer == recieverPlayer:
        return False
    else:
        senderPlayer.cobbleCoinHold -= amount
        senderPlayer.save()

        recieverPlayer.cobbleCoinHold += amount
        recieverPlayer.save()

        return True
