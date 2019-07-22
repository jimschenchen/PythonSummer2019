import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

#key up down events
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE and len(bullets) < ai_settings.bullet_allowed:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        pygame.quit()
        sys.exit()
def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False    

#check events
def check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)
            
def check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    button_checked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_checked and not stats.game_active:
        stats.reset_stats()
        stats.game_active = True
        
        pygame.mouse.set_visible(False)
        
        aliens.empty()
        bullets.empty()
        
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
            
            
            
def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    #Screen color
    screen.fill(ai_settings.bg_color)
    
    #Screen ship
    ship.blitme()
    
    #Alien
    #alien.blitme()
    aliens.draw(screen)
    
    #Bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        
    #scoreboard
    sb.show_score()
    
    if not stats.game_active:
        play_button.draw_button()
    
    #Screen display
    pygame.display.flip()
        
#Bullet
def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    #bullets move
    bullets.update()
    #Bullet remove out of bounder
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)   
            
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)         

            
def fire_bullet(ai_settings, screen, ship, bullets):
    new_bullet = Bullet(ai_settings, screen, ship)
    bullets.add(new_bullet)
    
#Alien_collon
def create_fleet(ai_settings, screen, ship, aliens):
    
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    
    for row_number in range(number_rows):
        for alien_number in range(get_number_aliens_x(ai_settings, alien_width)):
            create_alien(ai_settings, screen, aliens, alien_number, alien_width, row_number)

def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))    
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, alien_width, row_number):
    alien = Alien(ai_settings, screen)
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)
    
#Alien_row
def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height - 3 * (alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

#Alien Update
def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
        
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)
    
def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break
        
def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
    
#Collosions
def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    bullet_piercing = not ai_settings.piercing_bullet
    collisions = pygame.sprite.groupcollide(bullets, aliens, bullet_piercing, True) 
    
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)
    
    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)
        
#hit
def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    if stats.ship_left > 1:
        

        stats.ship_left -= 1
        print(stats.ship_left)
        aliens.empty()
        bullets.empty()
    
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
        
    

    
def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break
        
def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
