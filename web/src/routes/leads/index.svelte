<script>
	import Trash from '../../assets/icons/trash.svg';

	import { onMount } from 'svelte';
	import { api } from '$lib/utils';

	let leads = [];
	onMount(async () => {
		const response = await api('GET', 'leads');
		leads = await response.json();
	});
</script>

<template lang="pug">
  .w-full.h-full.flex.flex-col.pt-4
    .flex.justify-between.items-center
      .title
        | Leads
      .search.space-x-2.inline-flex.items-center()
        .action
          input.input(type="text" placeholder="Search")
        .action
            button.btn Next
        .action
            button.btn Prev

    .bg-white.mt-4.p-2.rounded-md
      table.min-w-full
        thead
          tr
            th(scope="col", align="left")
              | Phone
            th(scope="col", align="left")
              | FirstName
            th(scope="col", align="left")
              | LastName
        tbody
          +each('leads as lead')
            tr(class="last:border-b-0  hover:bg-gray-50")
              td
                | {lead.phone_work}
              td
                | {lead.first_name}
              td
                | {lead.last_name}

</template>
