<script>
	import LogoIcon from '../../assets/icons/logo.svg';
	import './navbar.css';
</script>

<template lang="pug">

nav.nav-top.bg-white.border-b
  .max-w-full.mx-auto
    .flex.items-center.justify-center.h-12
      .justify-between.flex.items-center(class='w-3/5')
        a.cursor-pointer(href='/')
          LogoIcon(width='2em' class="nav-link")
        .hidden(class='md:block')
          .ml-10.flex.items-baseline.space-x-6
            a.navlink(href='/leads') Leads
            a.navlink(href='/btc') Currency

</template>

<style>
	.nav-top {
		position: fixed;
		top: 0;
		left: 0;
		right: 0;
		z-index: 100;
	}
	.nav-top .navlink {
		-webkit-font-smoothing: antialiased;
		cursor: pointer;
	}
</style>
