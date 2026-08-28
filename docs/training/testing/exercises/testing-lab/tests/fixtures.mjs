export function fixture() {
  return {
    plan: { id: 'plan-1', source: 'inbox/demo.txt', destination: 'archive/demo.txt' },
    approval: { approved: true, planId: 'plan-1', expiresAt: 2000 },
    now: 1000
  };
}
