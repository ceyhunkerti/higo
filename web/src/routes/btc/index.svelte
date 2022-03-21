<script>
	import ApexCharts from 'apexcharts';
	import { onMount } from 'svelte';
	import { api } from '$lib/utils';

	onMount(() => {
		var data = [];
		var i = 0;
		function getNewSeries() {
			// api is not free enable this if you have a paid account, or find a free one
			// api('GET', 'currency').then(async (response) => {
			// 	let r = await response.json();
			// 	data.push({
			// 		x: Date.now(),
			// 		y: r["rate"]
			// 	});
			// 	if (data.length > 20) {
			// 		data.shift();
			// 	}
			// });
			data.push({
				x: Date.now(),
				y: 41091.7 + Math.random()
			});
			if (data.length > 20) {
				data.shift();
			}
		}

		var options = {
			chart: {
				height: 350,
				type: 'line',
				toolbar: {
					show: false
				},
				zoom: {
					enabled: false
				}
			},
			dataLabels: {
				enabled: false
			},
			stroke: {
				curve: 'smooth'
			},
			series: [
				{
					data: data
				}
			],
			title: {
				text: 'BTC Price',
				align: 'left'
			},
			markers: {
				size: 0
			},
			xaxis: {
				type: 'datetime'
			},
			yaxis: {
				forceNiceScale: true
			},
			legend: {
				show: false
			}
		};

		var chart = new ApexCharts(document.querySelector('#chart'), options);

		chart.render();

		window.setInterval(function () {
			getNewSeries();
			chart.updateSeries([
				{
					data: data
				}
			]);
		}, 3000);
	});
</script>

<div id="chart" class="w-full" />
