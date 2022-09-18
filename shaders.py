import pygame

def change_light_color(image,color):
    color_surf = pygame.Surface((image.get_width(),image.get_height()))
    color_surf.fill(color)
    image.blit(color_surf,(0,0),special_flags=pygame.BLEND_MULT)
    return image

class gradients:
    def rect():
        return 0

def blur(surface:pygame.Surface, amt):
    size = surface.get_size()
    new = pygame.Surface((int(size[0]*1.4),int(size[1]*1.4)),pygame.SRCALPHA,32).convert_alpha()
    new.blit(surface,(int(size[0]*0.2),int(size[1]*0.2)))
    surface = pygame.transform.smoothscale(new,(int(size[0]/amt),int(size[1]/amt)))
    surface = pygame.transform.smoothscale(surface,new.get_size())

    return surface, size[0]*0.15, size[1]*0.15