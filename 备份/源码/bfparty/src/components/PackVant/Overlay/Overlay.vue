<!-- name:Overlay 遮罩：加载遮罩 -->
<template>
  <Overlay
    :show="_show"
    :custom-style="{
      background: 'rgb(255, 255, 255, 0.6)',
      display: 'flex',
      justifyContent: 'center',
      alignItems:'center'
    }"
  >
    <Loading size="36px" color="#4994df" vertical type="spinner">
      <span style="color: #4994df">{{ props.title}}</span>
    </Loading>
  </Overlay>
</template>

<script setup>
/*  import
------------------------------------------------ */
import {watch, defineProps} from 'vue';
import {Loading, Overlay} from 'vant';

/*  data
------------------------------------------------ */
let _show = props.show;

/*  props
------------------------------------------------ */
const props = defineProps({
  title: {
    type: String,
    default: ''
  },
  show: {
    type: Boolean,
    default: false
  }
});

/*  侦听
------------------------------------------------ */
watch(() => props.show,(newV) => {
  _show = newV;
})
</script>

<style lang="scss" scoped>
</style>

<script>
export default {
  name: "VanOverlayLoading"
};
</script>