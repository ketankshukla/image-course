// Teaching model only. These objects are trusted fixtures, not signed credentials.
export function mayExecute(plan, approval, now) {
  if (!approval) return false;
  return Boolean(
    approval.approved &&
    approval.planId === plan.id &&
    approval.expiresAt >= now
  );
}

export async function executePlan(plan, approval, { now, move }) {
  if (!mayExecute(plan, approval, now)) return { status: 'denied' };
  await move(plan.source, plan.destination);
  return { status: 'completed' };
}
