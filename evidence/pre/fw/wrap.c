#include <stdio.h>
#include "mock.h"
GPIO_TypeDef GPIOA_obj, GPIOC_obj;
static uint32_t tick; static int led=0; static FILE*lg;
uint32_t HAL_GetTick(void){return tick;}
GPIO_PinState HAL_GPIO_ReadPin(GPIO_TypeDef*p,uint16_t n){(void)p;(void)n;return GPIO_PIN_RESET;}
void HAL_GPIO_TogglePin(GPIO_TypeDef*p,uint16_t n){(void)p;(void)n;led=!led;fprintf(lg,"%u\n",tick);}
#include "routine_excerpt.c"
int main(void){lg=fopen("wrap_log.txt","w"); uint32_t start=0xFFFFFFFFu-4500u; /* 래핑 직전부터 */
 /* 먼저 한 번 호출해 last_toggle_ms를 현재 시각 근처로 맞춘다 */
 for(uint32_t k=0;k<12000;k++){ tick=start+k; polling_routine(); } fclose(lg); return 0;}
