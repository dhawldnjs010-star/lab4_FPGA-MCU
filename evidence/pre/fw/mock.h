#include <stdint.h>
typedef enum { GPIO_PIN_RESET = 0, GPIO_PIN_SET = 1 } GPIO_PinState;
typedef struct { int dummy; } GPIO_TypeDef;
extern GPIO_TypeDef GPIOA_obj, GPIOC_obj;
#define GPIOA (&GPIOA_obj)
#define GPIOC (&GPIOC_obj)
#define GPIO_PIN_5  5U
#define GPIO_PIN_13 13U
#define LED_ece2_Pin GPIO_PIN_5
#define LED_ece2_GPIO_Port GPIOA
#define BUTTON_ece2_Pin GPIO_PIN_13
#define BUTTON_ece2_GPIO_Port GPIOC
uint32_t HAL_GetTick(void);
GPIO_PinState HAL_GPIO_ReadPin(GPIO_TypeDef*, uint16_t);
void HAL_GPIO_TogglePin(GPIO_TypeDef*, uint16_t);
