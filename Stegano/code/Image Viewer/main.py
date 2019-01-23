if __name__ == '__main__':

    import sys
    from app.Orlo import Orlo

    player = Orlo(sys.argv) 
    sys.exit(player.run())
