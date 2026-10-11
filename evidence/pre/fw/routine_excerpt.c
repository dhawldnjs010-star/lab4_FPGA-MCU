/* STM32_0 과제1·2: 버튼으로 간격 1->2->4->8->1초
 * 과제1: 내장 LED(PA5). 과제2는 아래 두 줄을
 * GPIO_OUT1_ece2_Pin, GPIO_OUT1_ece2_GPIO_Port
 * (PB0)로 바꾼다. */
#define BLINK_LED_Pin        LED_ece2_Pin
#define BLINK_LED_GPIO_Port  LED_ece2_GPIO_Port
#define DEBOUNCE_MS          200U

void polling_routine(void)
{
    static const uint32_t interval_ms[4] =
        {1000U, 2000U, 4000U, 8000U};
    static uint8_t  idx = 0U;         /* 간격 번호 */
    static uint32_t last_toggle_ms = 0U;  /* 마지막 반전 */
    static uint32_t last_press_ms = 0U;   /* 마지막 입력 */
    static GPIO_PinState previous = GPIO_PIN_RESET;

    uint32_t now = HAL_GetTick();
    GPIO_PinState current = HAL_GPIO_ReadPin(
        BUTTON_ece2_GPIO_Port, BUTTON_ece2_Pin);

    /* LOW->HIGH 순간만, 200 ms 안의 재검출은 무시 */
    if ((previous == GPIO_PIN_RESET) &&
        (current == GPIO_PIN_SET) &&
        ((now - last_press_ms) >= DEBOUNCE_MS))
    {
        idx = (uint8_t)((idx + 1U) % 4U);
        last_press_ms = now;
    }
    previous = current;

    /* 간격이 지나면 LED 반전 (버튼과 무관) */
    if ((now - last_toggle_ms) >= interval_ms[idx])
    {
        last_toggle_ms = now;
        HAL_GPIO_TogglePin(BLINK_LED_GPIO_Port,
                           BLINK_LED_Pin);
    }
}

