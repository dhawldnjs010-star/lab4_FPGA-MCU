#include <stdio.h>
#include "mock.h"
GPIO_TypeDef GPIOA_obj, GPIOC_obj;
static uint32_t tick = 0; static int btn = 0; static int led = 0; static FILE *lg;
uint32_t HAL_GetTick(void){ return tick; }
GPIO_PinState HAL_GPIO_ReadPin(GPIO_TypeDef*p, uint16_t n){ (void)p;(void)n; return btn?GPIO_PIN_SET:GPIO_PIN_RESET; }
void HAL_GPIO_TogglePin(GPIO_TypeDef*p, uint16_t n){ (void)p;(void)n; led=!led; fprintf(lg,"T %u %d\n",tick,led); }
#include "routine_excerpt.c"
/* 버튼 파형: 시작 시각(ms), 길이(ms) 목록. 첫 항목은 바운스 포함 시험 */
typedef struct { uint32_t t0, t1; } Pulse;
static const Pulse pulses[] = {
  {3000,3010},{3030,3040},{3060,3600},   /* 한 번 누름 + 접점 떨림 2회(200 ms 이내) */
  {10000,15000},                         /* 5초 동안 길게 누름 */
  {22000,22300},{30000,30300},{50000,50300}, /* 이후 3번 더 */
};
int main(void){
  lg=fopen("fw_log.txt","w");
  for(tick=0; tick<=120000; tick++){
    btn=0;
    for(unsigned k=0;k<sizeof pulses/sizeof pulses[0];k++) if(tick>=pulses[k].t0 && tick<pulses[k].t1) btn=1;
    static int pb=-1; if(btn!=pb){ fprintf(lg,"B %u %d\n",tick,btn); pb=btn; }
    polling_routine();
  }
  fclose(lg); return 0; }
